Как запускать

Нужные либы подгружаем из requirements.txt автоматически

В mining_test_app создаем файл local_settings.py и
 пишем туда все локальные настройки
А именно

DEBUG
ALLOWED_HOSTS
DATABASES

##########################
Пример local_settings.py

DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mining_test',
        'USER' : 'username',
        'PASSWORD' : 'password',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
}

###########################

О приложении
По эндпоинту /resources/
Методы GET для получения списка, post для добавления

Для метода POST
    {
        "title": "Some another title",
        "amount": 20,
        "measure": "kg",
        "price": 300.0,
        "date": "2021-10-10"
    }

/resources/<id> для PUT и DELETE соответсвенно

для partial update юзаем PATCH

/total_cost/ возвращает /total_cost