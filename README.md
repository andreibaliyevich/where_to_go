# where_to_go


### Where to go - сайт-приложение, помогающее найти на карте интересные места в вашем городе.

[Cсылка на работающий сайт](https://andreibaliyevich.pythonanywhere.com/)


## Описание проекта

Места на карте добавляются через административный сайт Django. К местам, имеется возможность загружать фотографии. Они отображаются во всплывающих карточках.


## Установка

Для запуска проекта испльзуется виртуальное окружение.

##### 1. Клонировать репозиторий

    git clone https://github.com/andreibaliyevich/where_to_go.git

##### 2. Перейти в папку репозитория

    cd where_to_go

##### 3. Создать файл .env с переменными окружения в папке where_to_go

Например:

    SECRET_KEY='Vash-secretniy-kluch'
    DEBUG=true

##### 4. Создать виртуальное окружение

    python -m venv venv

##### 5. Запустить виртуальное окружение

    source venv/bin/activate

##### 7. Установить зависимости

    pip install -r requirements.txt

##### 8. Создать суперпользователя

    python manage.py createsuperuser

##### 9. Запустить приложение

    python manage.py runserver 
