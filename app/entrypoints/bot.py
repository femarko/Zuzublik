import telebot

import app.config
from app.service_layer import app_manager
from app.auxiliary_services import parser, validation
from app.service_layer.unit_of_work import UnitOfWork
from app.orm_tool.sql_aclchemy_wrapper import orm_conf

orm_conf.start_mapping()

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
    save_res = app_manager.add_zuzublik(
        file=downloaded_file, parser=parser.parse_table, validator=validation.validate_zuzublik_data, uow=UnitOfWork()
    )
    bot.send_message(message.chat.id, text=f'You uploaded the folowing data: {save_res[1]}.')


bot.polling(none_stop=True)