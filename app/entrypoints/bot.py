import telebot
from emoji import emojize

import app.config
from app.service_layer import app_manager
from app.auxiliary_services import parser, validation
from app.service_layer.unit_of_work import UnitOfWork
from app.orm_tool.sql_aclchemy_wrapper import orm_conf
from app.domain import errors


bot = telebot.TeleBot(app.config.config["bot_token"])

smth_went_wrong_message = f'Ой, что-то пошло не так...{emojize(":face_with_rolling_eyes:")}\n\nВозможно, неверный '\
                            'формат файла. Я умею работать только с файлами Excel.\n\nЧтобы попробовать снова, '\
                                                                         'нажми "Меню" - голубая кнопка внизу.'


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="Загрузить зюзюбликов", callback_data="upload_excel"))
    bot.send_message(message.chat.id, text='Хочешь загрузить своих зюзюбликов?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'upload_excel':
        callback_upload_excel(call)


def callback_upload_excel(call):
    bot.send_message(call.message.chat.id, 'Пожалуйста, отправь мне свой файл Excel.')
    bot.register_next_step_handler(call.message, handle_file)


def handle_file(message):
    try:
        file_id = message.document.file_id
    except AttributeError:
        bot.send_message(message.chat.id, text=smth_went_wrong_message)
        return
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)
    happy_way_reply = ""
    try:
        save_res = app_manager.add_zuzublik(
            file=downloaded_file, parser=parser.parse_table, validator=validation.validate_zuzublik_data,
            uow=UnitOfWork()
        )
        for item in save_res[1]:
            happy_way_reply += f"{item}\n"
        bot.send_message(message.chat.id, text=f'Готово! {emojize(":thumbs_up:")}\n\n'
                                               f'Вот что я загрузил:\n\n{happy_way_reply}.')
    except errors.ValidationError as e:
        bot.send_message(message.chat.id, text=f"Ой, кажется, данные в таблице некорректны. "
                                               f"Не могу загрузить {emojize(':face_with_rolling_eyes:')}\n"
                                               f"Ниже - подробнее, в чем проблема.\n\n"
                                               f"Чтобы загрузить исправленную таблицу, нажми "
                                               f"'Меню' - голубая кнопка внизу.\n\n"
                                               f"Подробности об ошибке:\n\n{e.message}\n\n"
                                               f"* type - тип ошибки\n"
                                               f"* loc - поле с некорректными данными\n"
                                               f"* msg - суть проблемы\n"
                                               f"* input - некорректное значение в таблице")
    except errors.SmthWentWrong:
        bot.send_message(message.chat.id, text=smth_went_wrong_message)



if __name__ == '__main__':
    orm_conf.start_mapping()
    bot.polling(none_stop=True)
