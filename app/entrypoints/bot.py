import telebot

import app.config

bot_funcs = telebot.TeleBot(app.config.config["bot_token"])


# @bot_funcs.message_handler(content_types=["text"])
# def get_text_messages(message):
#     bot_funcs.reply_to(message, message.text)

@bot_funcs.message_handler(commands=["start"])
def start_bot(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.add(telebot.types.KeyboardButton("Upload Excel file", request_contact=True))
    bot_funcs.send_message(message.chat.id, "Please click the button to upload an Excel file", reply_markup=markup)




# @bot_funcs.message_handler(commands=["start"])
# def start_bot(message):
#     markup = telebot.types.ReplyKeyboardMarkup()
#     upload_xls_button = telebot.types.ReplyKeyboardMarkup("Upload Excel file", callback_data="upload_xls")
#     markup.add(upload_xls_button)
#     bot_funcs.send_message(message.chat.id, "Please click the button to upload an Excel file", reply_markup=markup)

# @bot_funcs.message_handler(content_types=["text"])
# def echo_all(message):
#     bot_funcs.send_message(message.chat.id, message.text)


# # Create a keyboard markup with a single button
# keyboard = telebot.types.InlineKeyboardMarkup()
# button = telebot.types.InlineKeyboardButton('Send Excel file', callback_data='send_excel')
# keyboard.add(button)
#
# # Send the keyboard to the user
# bot_funcs.send_message(message.chat.id, 'Please click the button to send an Excel file', reply_markup=keyboard)


bot_funcs.polling(none_stop=True)