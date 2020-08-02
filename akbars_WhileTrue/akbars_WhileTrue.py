import telebot

import random

from telebot import types

bot = telebot.TeleBot('1208274828:AAHEqmnQDAPGa-16ibojQI9LtC_eIWfptws')

@bot.message_handler(commands=['start'])
def start_message(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Потребительский кредит')
    item2 = types.KeyboardButton('Банковская карта')
    item3 = types.KeyboardButton('Ипотека')
    item4 = types.KeyboardButton('Вклад')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}!\nЯ - <b>{1.first_name}</b>, '
                                      'Выберите продукт банка, который хотите оформить'.format(message.from_user,
                                       bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Потребительский кредит':
            bot.send_message(message.chat.id, 'Введите сумму кредита от 300 тысяч рублей до 2 миллионов рублей?')
        elif message.text == 'Банковская карта':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item5 = types.InlineKeyboardButton('Дебетовая карта', callback_data='good')
            item6 = types.InlineKeyboardButton('Кредитная карта', callback_data='bad')
            markup.add(item5, item6)
            bot.send_message(message.chat.id, 'Выберите нужный формат', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Выбрана дебет карта')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Выбрана кредит карта')
            # remove inline button
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Условия подачи онлайн-заявки", reply_markup=None)
            # show alert
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='Это тестовое уведомление')
    except Exception as e:
        print(repr(e))
# RUN
if __name__ == '__main__':
     bot.polling(none_stop=True)