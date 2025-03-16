import telebot

import app.config

bot = telebot.TeleBot(app.config.config["bot_token"])

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="Upload Excel file", callback_data="upload_excel"))
    bot.send_message(message.chat.id, text='Hello! Want to upload your zuzubles?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'upload_excel':
        callback_upload_excel(call)


def callback_upload_excel(call):
    bot.send_message(call.message.chat.id, 'Please upload your Excel file')
    bot.register_next_step_handler(call.message, handle_file)


def handle_file(message):
    file_id = message.document.file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)
    bot.send_message(message.chat.id, 'File uploaded successfully!')



bot.polling(none_stop=True)