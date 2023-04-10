## Установка
1. Копируйте репозиторий с github
2. Создайте виртуальное окружение 
3. Установите зависимости `pip install -r requirements.txt`
4. Запустите в cmd сервер `python manage.py runserver`
5. Создайте в PostrgreSQL пользователя и базу данных
   и впишите данные в файл `settings.py`
```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'имя БД',
        'USER': 'имя владельца БД',
        'PASSWORD': 'пароль БД',
        'HOST': 'localhost',
        'PORT': 'порт БД',
    }
}
```
## Запуск программы
1. Создайте superuser через cmd - администратор портала
    1.1 Войдите в директорию LearnHub и активируйте 
        виртуальное окружение `venv\Scripts\activate`
    2.2 Перейдите в cmd в portal c файлом `manage.py`
    3.3 Мигрируйте данные `python manage.py  migrate`
    4.4 Создайте superuser `python manage.py createsuperuser`
    5.5 Заполните данные Администратора портала логин и пароль.
2. Запустите портал `python manage.py runserver`