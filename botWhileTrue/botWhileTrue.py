import telebot
import requests
from telebot import types

token = '1208274828:AAHEqmnQDAPGa-16ibojQI9LtC_eIWfptws'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    # выводим клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Вклад')
    item2 = types.KeyboardButton('Кредит')
    item3 = types.KeyboardButton('Ипотека')
    item4 = types.KeyboardButton('Дебетовые карты')
    item5 = types.KeyboardButton('Статус заявки')
    item6 = types.KeyboardButton('Специалист')
    markup.add(item1, item2, item3, item4, item5, item6)
    # приветствие после команды /start
    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}!\nВас приветствует - <b>{1.first_name}</b>.\n \n'
                                      'Выберите необходимый пункт меню:\n'
                                      '/status - Ваши заявки'.format(message.from_user,
                                                                               bot.get_me()), parse_mode='html',
                     reply_markup=markup)

"""Для проверки статуса уже сделанной заявки"""
@bot.message_handler(commands=['status'])
def status(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    # button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Отправьте свой номер телефона", reply_markup=keyboard)


@bot.message_handler(content_types=['text', 'document', 'photo'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Вклад':
            markup_vklad = types.InlineKeyboardMarkup(row_width=1)
            item7 = types.InlineKeyboardButton('Уверенное будущее до 6,3%*', callback_data='vklad_future')
            item8 = types.InlineKeyboardButton('Я сам?! до 5,8%*', callback_data='vklad_self')
            item9 = types.InlineKeyboardButton('Просто преумножить до 5%*', callback_data='vklad_mnzh')
            item10 = types.InlineKeyboardButton('Просто поймай момент до 2,95%*', callback_data='vklad_moment')
            item11 = types.InlineKeyboardButton('Просто управлять до 4,6%*', callback_data='vklad_upr')
            item12 = types.InlineKeyboardButton('Просто накопить до 5,1%*', callback_data='vklad_nakop')
            markup_vklad.add(item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Выберите необходимую вам программу:', reply_markup=markup_vklad)

        elif message.text == 'Кредит':
            markup_kredit = types.InlineKeyboardMarkup(row_width=1)
            item13 = types.InlineKeyboardButton('Помощь в период COVID-19', callback_data='kredit_covid19')
            item14 = types.InlineKeyboardButton('Кредит наличными до 7 лет', callback_data='kredit_cash')
            item15 = types.InlineKeyboardButton('Кредит до 20 лет', callback_data='kredit_zalog')
            item16 = types.InlineKeyboardButton('Рефинансирование кредитов', callback_data='kredit_ref')
            item17 = types.InlineKeyboardButton('Кредитная карта Emotion', callback_data='kredit_card')
            markup_kredit.add(item13, item14, item15, item16, item17)
            bot.send_message(message.chat.id, 'Выберите удобную вам программу:', reply_markup=markup_kredit)

        elif message.text == 'Ипотека':
            markup_ipoteka = types.InlineKeyboardMarkup(row_width=1)
            item18 = types.InlineKeyboardButton('Вторичное жилье', callback_data='ipoteka_vtor')
            item19 = types.InlineKeyboardButton('Новостройки с господдержкой', callback_data='ipoteka_novogos')
            item20 = types.InlineKeyboardButton('Новостройки', callback_data='ipoteka_novo')
            item21 = types.InlineKeyboardButton('Рефинансирование ипотеки', callback_data='ipoteka_ref')
            item22 = types.InlineKeyboardButton('Господдержка для семей с детьми', callback_data='ipoteka_child')
            item23 = types.InlineKeyboardButton('Коммерческая недвижимость', callback_data='ipoteka_kom')
            item24 = types.InlineKeyboardButton('Дом и земельный участок', callback_data='ipoteka_house')
            markup_ipoteka.add(item18, item19, item20, item21, item22, item23, item24)
            bot.send_message(message.chat.id, 'Выберите нужную вам программу', reply_markup=markup_ipoteka)

        elif message.text == 'Дебетовые карты':
            markup_card = types.InlineKeyboardMarkup(row_width=1)
            item25 = types.InlineKeyboardButton('Карта Aurum', callback_data='card_aurum')
            item26 = types.InlineKeyboardButton('Карта Evolution', callback_data='card_evolution')
            item27 = types.InlineKeyboardButton('Карта Generation', callback_data='card_generation')
            item28 = types.InlineKeyboardButton('Ак Барс Premium', callback_data='card_premium')
            item29 = types.InlineKeyboardButton('Классическая карта', callback_data='card_classic')
            item30 = types.InlineKeyboardButton('Мир Долголетия', callback_data='card_mir')
            markup_card.add(item25, item26, item27, item28, item29, item30)
            bot.send_message(message.chat.id, 'Выберите удобную вам программу:', reply_markup=markup_card)

        elif message.text == 'Специалист':
            '''не работает'''
            bot.send_message(message.chat.id, 'Отправлен запрос на консультацию.\nВ ближайшее время с вами свяжется специалист банка..')
            bot.send_message(chat_id=71404035, text=f'Клиент @{message.from_user.username} просит начать консультацию')

        elif message.text == 'Статус заявки':
            # просим поделиться телефоном вызвав функцию status()
            # или чтобы клиент написал номер заявки и ищем в своей базе данных
            bot.send_message(message.chat.id, 'У вас нет заявок')

        else:
            bot.send_message(message.chat.id, 'Неверная команда')


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