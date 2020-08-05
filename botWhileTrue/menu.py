from telebot import types

start = [
    types.KeyboardButton('Вклад'),
    types.KeyboardButton('Кредит'),
    types.KeyboardButton('Ипотека'),
    types.KeyboardButton('Дебетовые карты'),
    types.KeyboardButton('Статус заявки'),
    types.KeyboardButton('Специалист')
]

services =  {
    "Вклад": [
        types.InlineKeyboardButton('Уверенное будущее до 6,3%*', callback_data='vklad_future'),
        types.InlineKeyboardButton('Я сам?! до 5,8%*', callback_data='vklad_self'),
        types.InlineKeyboardButton('Просто преумножить до 5%*', callback_data='vklad_mnzh'),
        types.InlineKeyboardButton('Просто поймай момент до 2,95%*', callback_data='vklad_moment'),
        types.InlineKeyboardButton('Просто управлять до 4,6%*', callback_data='vklad_upr'),
        types.InlineKeyboardButton('Просто накопить до 5,1%*', callback_data='vklad_nakop')
    ],
    "Кредит": [
        types.InlineKeyboardButton('Помощь в период COVID-19', callback_data='kredit_covid19'),
        types.InlineKeyboardButton('Кредит наличными до 7 лет', callback_data='kredit_cash'),
        types.InlineKeyboardButton('Кредит до 20 лет', callback_data='kredit_zalog'),
        types.InlineKeyboardButton('Рефинансирование кредитов', callback_data='kredit_ref'),
        types.InlineKeyboardButton('Кредитная карта Emotion', callback_data='kredit_card')
    ],
    "Ипотека": [
        types.InlineKeyboardButton('Вторичное жилье', callback_data='ipoteka_vtor'),
        types.InlineKeyboardButton('Новостройки с господдержкой', callback_data='ipoteka_novogos'),
        types.InlineKeyboardButton('Новостройки', callback_data='ipoteka_novo'),
        types.InlineKeyboardButton('Рефинансирование ипотеки', callback_data='ipoteka_ref'),
        types.InlineKeyboardButton('Господдержка для семей с детьми', callback_data='ipoteka_child'),
        types.InlineKeyboardButton('Коммерческая недвижимость', callback_data='ipoteka_kom'),
        types.InlineKeyboardButton('Дом и земельный участок', callback_data='ipoteka_house')
    ],
    "Дебетовые карты": [
        types.InlineKeyboardButton('Карта Aurum', callback_data='card_aurum'),
        types.InlineKeyboardButton('Карта Evolution', callback_data='card_evolution'),
        types.InlineKeyboardButton('Карта Generation', callback_data='card_generation'),
        types.InlineKeyboardButton('Ак Барс Premium', callback_data='card_premium'),
        types.InlineKeyboardButton('Классическая карта', callback_data='card_classic'),
        types.InlineKeyboardButton('Мир Долголетия', callback_data='card_mir')
    ]
}

service_messages = [
    "Выберите необходимую вам программу:",
    "Выберите удобную вам программу:",
    "Выберите нужную вам программу"
]
