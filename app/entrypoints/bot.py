import telebot

import app.config

bot = telebot.TeleBot(app.config.config["bot_token"])

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="Upload Excel file", callback_data="upload_excel"))
    bot.send_message(message.chat.id, text='Hello! Want to upload your zuzubles?', reply_markup=markup)


bot.polling(none_stop=True)