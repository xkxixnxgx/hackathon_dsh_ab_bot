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
user = {}


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


@bot.message_handler(content_types=['text', 'document', 'photo'])
def lalala(message: types.Message):
    if message.chat.type == 'private':
        user_message = message.text
        
        try:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(*menu.services[user_message])
            bot.send_message(message.chat.id, choice(menu.service_messages), reply_markup=markup)
            
            user['chat_id'] = message.chat.id
            user["service"] = user_message
        except KeyError:
            bot.send_message(message.chat.id, 'Неверная команда')


# Оформить заявку
@bot.callback_query_handler(func=lambda call: call.data == 'submit')
def submit(call):
    pass


# Назад
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(call):
    proposal = call.data
    print(proposal)
    message = call.message
    message.text = user['service'] # Текущий сервис
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(*menu.services[message.text])

    bot.edit_message_text(
        choice(menu.service_messages), 
        call.message.chat.id, 
        call.message.message_id, reply_markup=markup
    )


# Обработка предложений
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        try:
            proposal = call.data
            user['proposal'] = menu.proposals[proposal]['name']
            print(user)

            markupupup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Оставить заявку", callback_data='submit')
            item2 = types.InlineKeyboardButton("Назад", callback_data='back')
            markupupup.add(item1, item2)

            #bot.send_message(call.message.chat.id, menu.proposals[proposal], reply_markup=markupupup)
            bot.edit_message_text(
                f"{menu.proposals[proposal]['message']}:\n{menu.proposals[proposal]['link']}", 
                call.message.chat.id, 
                call.message.message_id, reply_markup=markupupup
            )
        except KeyError:
            bot.send_message(call.message.chat.id, "В разработке")

# СТАРТ
if __name__ == '__main__':
     bot.polling(none_stop=True)
