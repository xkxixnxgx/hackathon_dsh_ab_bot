import sys # модуль для взаимодействия с системными функциями, для корректного завершения функций

from webapp import create_app
from webapp.db import db
from webapp.user.models import Requests
from datetime import datetime

app = create_app()

with app.app_context(): # строка после которой можно работать с базой данных
    product = input('Product: ')
    date_now = datetime.now()
    date_add = date_now.strftime('%d.%m.%Y')
    status_request = 'considers'
    first_name_client = input('Write u first name: ')
    last_name_client = input('Write u last name: ')
    passport_series = input('Write u passport series: ')
    passport_number = input('Write u passport number: ')
    phone_client = input('Write u phone number:')

    if Requests.query.filter(Requests.phone_client == phone_client).count():
        print('A user with the same phone already exists.')
        sys.exit(0)

    new_request = Requests(
        product=product,
        date_add=date_add,
        status_request=status_request,
        first_name_client=first_name_client,
        last_name_client=last_name_client,
        passport_series=passport_series,
        passport_number=passport_number,
        phone_client=phone_client
    )

    db.session.add(new_request)
    db.session.commit()
    print('Request with id={} added'.format(new_request.id))

