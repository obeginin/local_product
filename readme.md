# local_project
мой небольшой локальный проект

Шаги для установки проекта:
1) pip install --upgrade pip (обновляем менеджер пакетов pip до послдней верси)
2) pip install django (устанавливаем Django)
3) pip install djangorestframework (устанавиаем библиотеку REST для работ с API)
4) django-admin startproject loc (создаем Django приложени loc)
5) sudo apt install postgresql postgresql-contribib (устанавливаем PostgresSQL с дп модулями)
6) sudo apt install libpq-dev python3-dev (устанавливаем пакет необходимый для работы psycopg2 и другие модули)
7) pip install psycopg2 (Устанавливем библиотеку psycopg2, которая позволяет Python-приложению взаимодействовать с PostgreSQL)
8) создал базу данных: local_db, с таблицей local_table
9) python manage.py createsuperuser (Создаем супепользователя для полного доступа к БД логин:oleg пароль:oleg)
10) python manage.py migrate (Выполняем миграции БД) в данном случае для админки, аворизации
11) pip install django-environ (Устанавливаем библиотеку для работы с переменным окружением, файл .env)