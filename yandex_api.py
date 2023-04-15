# -*- coding: utf-8 -*-

import json
import time

import requests

from config_reader import config

# Укажите ваш API-ключ и ссылку на аудиофайл в Object Storage.
key = config.yandex_aim.get_secret_value()
filelink = 'https://storage.yandexcloud.net/speechkit/speech.ogg'

POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"

body = {
    "config": {
        "specification": {
            "languageCode": "ru-RU"
        }
    },
    "audio": {
        "uri": filelink
    }
}

header = {'Authorization': 'Bearer {}'.format(key)}

# Отправить запрос на распознавание.
req = requests.post(POST, headers=header, json=body)
data = req.json()
print(data)

id = data['id']

# Запрашивать на сервере статус операции, пока распознавание не будет завершено.
while True:

    time.sleep(1)

    GET = "https://operation.api.cloud.yandex.net/operations/{id}"
    req = requests.get(GET.format(id=id), headers=header)
    req = req.json()

    if req['done']:
        break
    print("Not ready")

# Показать полный ответ сервера в формате JSON.
print("Response:")
print(json.dumps(req, ensure_ascii=False, indent=2))

# Показать только текст из результатов распознавания.
print("Text chunks:")
for chunk in req['response']['chunks']:
    print(chunk['alternatives'][0]['text'])
