import telebot

import app.config

bot_funcs = telebot.TeleBot(app.config.config["bot_token"])


@bot_funcs.message_handler(content_types=["text"])
def get_text_messages(message):
    bot_funcs.reply_to(message, message.text)


# @bot_funcs.message_handler(content_types=["text"])
# def echo_all(message):
#     bot_funcs.send_message(message.chat.id, message.text)

bot_funcs.polling(none_stop=True)