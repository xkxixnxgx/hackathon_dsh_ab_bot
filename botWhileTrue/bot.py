import telebot # pytelegrambotapi
import requests
from telebot import types
from random import choice
import menu
import questions

# token = '1208274828:AAHEqmnQDAPGa-16ibojQI9LtC_eIWfptws'
token = '1340902997:AAH0MDN5eLDNbi74QRRaooM9gojRGEuZMds'
bot = telebot.TeleBot(token)


registration = False
registration_form = None
current_question = None

user = {
    "chat_id": "",
    "username": "",
    "service": "",
    "proposal": "",
    "status": "",
    "data": {},
}



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


# Сервисы
@bot.message_handler(
    content_types=['text', 'document', 'photo'],
    func=lambda x : registration == False)
def services(message: types.Message):
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


# Отмена заявки
@bot.message_handler(regexp=r'^Отмена$', func=lambda x: registration == True)
def cancel(message):
    global registration
    registration = False

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    markup.add(*menu.start)
    bot.send_message(message.chat.id, "Заявка отменена. Данные не сохранены.", reply_markup=markup)


# Оформить заявку
@bot.callback_query_handler(func=lambda call: call.data == 'submit')
def submit(call):
    global registration_form, registration, current_question
    registration = True
    registration_form = questions.start(user['service'])

    first_question = next(registration_form)
    current_question = first_question[0]
    bot.send_message(call.message.chat.id, first_question[1])


# Регистрация
@bot.message_handler(func=lambda x: registration == True)
def reg(message):
    try:
        global current_question, registration
        user['data'][current_question] = message.text

        item = next(registration_form)
        current_question = item[0]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Отмена"))
        markup.add(types.KeyboardButton("Пропустить"))
        bot.send_message(message.chat.id, item[1], reply_markup=markup)
    except StopIteration:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        markup.add(*menu.start)

        bot.send_message(message.chat.id, "Заявка принята", reply_markup=markup)

        registration = False
        # TODO: Функция передачи заявки в базу данных
        print(user)


# Назад
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(call):
    # proposal = call.data

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
    bot.polling(none_stop=True, interval=0)
