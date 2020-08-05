import telebot # pytelegrambotapi
import requests
from telebot import types
from random import choice
import menu
# token = '1208274828:AAHEqmnQDAPGa-16ibojQI9LtC_eIWfptws'
token = '1340902997:AAH0MDN5eLDNbi74QRRaooM9gojRGEuZMds'
bot = telebot.TeleBot(token)

quest = ["Номер телефона", "Ф.И.О.", "Город", "Любимый цвет"]
quest_count = 0
registration = False
reg_form = {}

# Тестовая функция регистрации
@bot.message_handler(commands=['reg'])
def reg(message):
    global registration, reg_form, quest_count
    registration = True
    reg_form = {}
    quest_count = 0
    reg_form['chat_id'] = message.chat.id
    # keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    # button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    # keyboard.add(button_phone)
    # bot.send_message(message.chat.id, f"Укажите {quest[quest_count]}", reply_markup=keyboard)
    

@bot.message_handler(func=lambda x: registration == True)
def reg_proc(message):
    global reg_form, quest_count, registration
    count = quest_count
    answer = message.text
    reg_form[quest[count]] = answer

    if count < len(quest) - 1:
        quest_count += 1
        bot.send_message(message.chat.id, f"Укажите {quest[quest_count]}")
    else:
        print(reg_form)
        registration = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        markup.add(*menu.start)
        bot.send_message(message.chat.id, "Зпасибо за регистрацию", reply_markup=markup)



@bot.message_handler(commands=['start'])
def start_message(message):
    # выводим клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    markup.add(*menu.start)

    text = "".join([
        f"Здравствуйте, {message.from_user.first_name}!\n",
        f"Вас приветствует - <b>{bot.get_me().first_name}</b>.\n\n",
        "Выберите необходимый пункт меню:\n",
        "/status - Ваши заявки"
    ])

    # приветствие после команды /start
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)

"""Для проверки статуса уже сделанной заявки"""
@bot.message_handler(commands=['status'])
def status(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    # button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Отправьте свой номер телефона", reply_markup=keyboard)

@bot.message_handler(regexp=r'^Заявки$')
def mumu(message):
    # просим поделиться телефоном вызвав функцию status()
    # или чтобы клиент написал номер заявки и ищем в своей базе данных
    bot.send_message(message.chat.id, 'У вас нет заявок')

# @bot.message_handler(regexp=r'^Специалист$')

@bot.message_handler(content_types=['text', 'document', 'photo'])
def lalala(message: types.Message):
    if message.chat.type == 'private':
        user_message = message.text
        
        try:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(*menu.services[user_message])
            bot.send_message(message.chat.id, choice(menu.service_messages), reply_markup=markup)
        except KeyError:
            bot.send_message(message.chat.id, 'Неверная команда')

        # elif message.text == 'Специалист':
        #     '''не работает'''
        #     bot.send_message(message.chat.id, 'Отправлен запрос на консультацию.\nВ ближайшее время с вами свяжется специалист банка..')
        #     bot.send_message(chat_id=71404035, text=f'Клиент @{message.from_user.username} просит начать консультацию')

        # elif message.text == 'Статус заявки':
        #     # просим поделиться телефоном вызвав функцию status()
        #     # или чтобы клиент написал номер заявки и ищем в своей базе данных
        #     bot.send_message(message.chat.id, 'У вас нет заявок')

        # else:

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # ВКЛАДЫ
            if call.data == 'vklad_future':
                markupupup = types.InlineKeyboardMarkup(row_width=1)
                item99 = types.InlineKeyboardButton('Оформить выбранный вклад', callback_data='carddd')
                markupupup.add(item99)
                bot.send_message(call.message.chat.id, 'Вклад с накопительным страхованием жизни: https://www.akbars.ru/individuals/deposits/uverennoe-budushchee/', reply_markup=markupupup)
            elif call.data == 'vklad_self':
                bot.send_message(call.message.chat.id, 'Вклад с пополнением и пролонгацией: https://www.akbars.ru/individuals/deposits/ya-sam/')
            elif call.data == 'vklad_mnzh':
                bot.send_message(call.message.chat.id, 'Вклад с пополнением и снятием: https://www.akbars.ru/individuals/deposits/prosto-preumnozhit/')
            elif call.data == 'vklad_moment':
                bot.send_message(call.message.chat.id, 'Вклад сроком на 31 день: https://www.akbars.ru/individuals/deposits/prosto-poimat-moment/')
            elif call.data == 'vklad_upr':
                bot.send_message(call.message.chat.id, 'Вклад с частичным снятием: https://www.akbars.ru/individuals/deposits/prosto-upravlyat/')
            elif call.data == 'vklad_nakop':
                bot.send_message(call.message.chat.id, 'Вклад с удобными процентами: https://www.akbars.ru/individuals/deposits/prosto-nakopit/')
            # КРЕДИТЫ
            elif call.data == 'kredit_covid19':
                bot.send_message(call.message.chat.id, 'Наши услуги и рекомендации для вас: https://www.akbars.ru/individuals/stay-home/')
            elif call.data == 'kredit_cash':
                bot.send_message(call.message.chat.id, 'От 7,7%*: https://www.akbars.ru/individuals/credits/potrebitelskiy/')
            elif call.data == 'kredit_zalog':
                bot.send_message(call.message.chat.id, 'Под залог недвижимости: https://www.akbars.ru/individuals/credits/potrebkredit-zalog-nedvizhimosti/')
            elif call.data == 'kredit_ref':
                bot.send_message(call.message.chat.id, 'Рефинансирование потребительских кредитов: https://www.akbars.ru/individuals/credits/refinansirovanie-potrebkreditov/')
            elif call.data == 'kredit_card':
                bot.send_message(call.message.chat.id, 'Льготный период, кэшбэк рублями и снятие наличных без комиссии: https://www.akbars.ru/individuals/credit-cards/emotion/')
            # ИПОТЕКИ
            elif call.data == 'ipoteka_vtor':
                bot.send_message(call.message.chat.id, 'Ставка от 7,75%: https://www.akbars.ru/individuals/hypothec/megapolis/')
            elif call.data == 'ipoteka_novogos':
                bot.send_message(call.message.chat.id, 'Ставка от 6,1%: https://www.akbars.ru/individuals/hypothec/subsidirovaniye-stavki/')
            elif call.data == 'ipoteka_novo':
                bot.send_message(call.message.chat.id, 'Ставка от 7,75%: https://www.akbars.ru/individuals/hypothec/perspektiva/')
            elif call.data == 'ipoteka_ref':
                bot.send_message(call.message.chat.id, 'Ставка от 7,99%: https://www.akbars.ru/individuals/hypothec/refinansirovanie-ipoteki/')
            elif call.data == 'ipoteka_child':
                bot.send_message(call.message.chat.id, 'Ставка от 4,9%: https://www.akbars.ru/individuals/hypothec/gospodderzhka-semya-s-detmi/')
            elif call.data == 'ipoteka_kom':
                bot.send_message(call.message.chat.id, 'Ставка от 9,99%: https://www.akbars.ru/individuals/hypothec/ak-bars-biznes/')
            elif call.data == 'ipoteka_house':
                bot.send_message(call.message.chat.id, 'Ставка от 8,5%: https://www.akbars.ru/individuals/hypothec/komfort/')
            # КАРТЫ
            elif call.data == 'card_aurum':
                bot.send_message(call.message.chat.id, 'Кэшбэк за покупки и процент на остаток выплачиваются золотом: https://www.akbars.ru/individuals/cards/aurum/')
            elif call.data == 'card_evolution':
                bot.send_message(call.message.chat.id, 'Самая выгодная карта для полетов по России*: https://www.akbars.ru/individuals/cards/evolution/')
            elif call.data == 'card_generation':
                bot.send_message(call.message.chat.id, 'Для тех, кто постоянно в движении: https://www.akbars.ru/individuals/cards/generation/')
            elif call.data == 'card_premium':
                bot.send_message(call.message.chat.id, 'Пакет услуг повышенной комфортности: https://www.akbars.ru/individuals/cards/ak-bars-premium/')
            elif call.data == 'card_classic':
                bot.send_message(call.message.chat.id, 'Универсальная карта для покупок: https://www.akbars.ru/individuals/cards/classic/')
            elif call.data == 'card_mir':
                bot.send_message(call.message.chat.id, 'Получайте пенсию на карту: https://www.akbars.ru/individuals/cards/mir-karta-dolgoletiya/')
            # убрать inline button
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Условия подачи онлайн-заявки https://andycoffee.ru/wp-content/uploads/akbarwhiletrue.pdf', reply_markup=None)

    except Exception as e:
        print(repr(e))


class Specialist:
    """Работа чат-специалиста"""
    pass


class NewZayavka:
    """Оформление новой заявки"""
    pass


# СТАРТ
if __name__ == '__main__':
     bot.polling(none_stop=True)