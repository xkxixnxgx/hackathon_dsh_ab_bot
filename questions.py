USER_BASE = [
    ('full_name', "Ф.И.О (Пример ввода: Иванов Иван Иванович)"),
    ('birthdate', "Дата рождения (ЧЧ.ММ.ГГ)"),
    ('birthplace', "Место рождения (Как в паспорте)"),
    ('passport_number', "Серия и номер паспорта (Пример ввода: 1234 567890)"),
    ('department_code', "Код подразделения (Пример ввода: 123-456)"),
    ('date_of_issue', "Дата выдачи (ЧЧ.ММ.ГГ)"),
    ('issued_by', "Кем выдан"),
    ('address', "Адрес регистрации (Как в паспорте)"),
    ('actual_address', "Фактический адрес жительства"),
    ('i_c', "СНИЛС (Пример ввода: 111-222-333 44)"),
    ('phone_number', "Мобильный телефон"),
    ('email', "Email")
]

def create_data_object(question_list):
    data_object = dict.fromkeys([k[0] for k in question_list])
    return data_object



# {
#     'full_name': "Иванов Иван Иванович",
#     'birthdate': "01.12.1995",
#     'birthplace': "Москва",
#     'passport_number': "1234 567890",
#     'department_code': "123-456",
#     'date_of_issue': "26.05.2009",
#     'issued_by': "Отделением ОУФМС",
#     'address': "Москва, ул. Тверская дом 3 кв. 127",
#     'actual_address': "",
#     'i_c': "111-222-333 44",
#     'phone_number': "+79094562565",
#     'email': "test@test.com"
# }