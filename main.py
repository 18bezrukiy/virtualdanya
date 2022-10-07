from aiogram import Bot, Dispatcher, executor, types
from google.cloud import dialogflow
import os
import logging

bot = Bot('5616233937:AAGz_7cbHI2CojJD82niwLO8cMIHfy8HYWA', parse_mode='HTML')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'assistent-83def-6f2c001354c0.json'

session_client = dialogflow.SessionsClient()
project_id = "assistent-83def"
session_id = 'session'
language_code = 'ru'
session = session_client.session_path(project_id, session_id)


@dp.message_handler(commands='start')
async def start(msg: types.Message):
    if msg.from_user.username == 'akl1ce':
        await bot.send_message(msg.from_user.id, 'Привет мась💕')
    else:
        await msg.answer('мне пофиг')


@dp.message_handler()
async def lzt_dialogflow(msg: types.Message):
    text_input = dialogflow.TextInput(text=msg.text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    if response.query_result.fulfillment_text:
        await msg.answer(response.query_result.fulfillment_text)
    else:
        await msg.answer('Рарзрабы не научили понимать это')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
