import asyncio
import logging

import openai
import speech_recognition as s_r
from aiogram import Bot, Dispatcher, types

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"
tg_token = "6001888812:AAE7ShWycoj8zG4m7xjvlxKm8xevsc--Rb0"

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=tg_token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я могу чем-то помочь тебе?")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


audio_file = s_r.AudioFile('my_clip.wav')



bot = Bot(token=tg_token)
dp = Dispatcher(bot=bot)

#print(openai.Model.list())
@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
)

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dispatcher=dp, skip_updates=True)