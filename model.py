from time import strftime

class User:
    full_name = ''
    birthdate = ''
    birthplace = ''
    passport_number = ''
    department_code = ''
    date_of_issue = ''
    issued_by = ''
    address = ''
    actual_address = ''
    i_c = ''
    phone_number = ''
    email = ''

class RequestBankService:
    chat_id = 0
    user_info = User()
    about_family = ''
    about_job = ''
    service_type = ''
    status = ''
    date = ''

    def create_obj(self):
        obj = self.__dict__
        obj['user_info'] = self.user_info.__dict__
        return obj

    def change_status(self, status: str):
        self.status = status
        self.date = strftime('%d:%m:%Y') 


class Status:
    accepted = 'Принято на рассмотрение'
    approved = 'Одобренно'
    decline = 'Отклоненно'

class ServiceType:
    bank_account = 'Открыть вклад'
    debit_card = 'Выпустить дебетовую карту'
    credit = 'Оформить кредит'
    mortgage = 'Оформить ипотеку'



