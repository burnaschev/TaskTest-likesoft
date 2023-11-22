# Тестовое задание 


## Эндпоинты

- Регистрация пользователя
- Авторизация пользователя
- Список книг
- Создание книги
- Редактирование книги
- Удаление книги


## Технологии

- Фреймворк Django Rest Framework
- База данных PostgreSQL
- Celery
- Язык программирования Python
- Git
- Docker
- Docker-compose

## Установка и запуск 

Следуйте этим шагам для установки и запуска проекта.

### Клонирование проекта

git clone https://github.com/burnaschev/DRF_project.git


### Создание и активация виртуального окружения

python3 -m venv venv
source venv/bin/activate

### Переменные окружения

Все необходимые переменные окружения находятся в файле .env_sample

Нужно создать свой переменные окружения в файле .env

### Установка зависимостей

pip install -r requirements.txt


### Запуск сервера 

python manage.py runserver

После чего вы сможете получить доступ к API по адресу `http://localhost:8000/`.


### Запуск Celery

- celery -A config worker -l INFO
- celery -A config beat -l INFO

## Docker

Если вы предпочитаете использовать Docker:

1. Соберите образ:

    ```bash
    docker-compose build
    ```

2. Запустите контейнер:

    ```bash
    docker-compose up -d
    ```

    Приложение будет доступно по адресу http://localhost:8080/.


## API Documentation swagger

API documentation can be found at `http://localhost:8000/docs/`.
