from telegram import Bot
import token_data

bot = Bot(token=token_data.TOKEN)
chat_id = token_data.CHAT_ID
text = 'Вам телеграмма!'
bot.send_message(chat_id, text)
