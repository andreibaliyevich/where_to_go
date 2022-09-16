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
    ALLOWED_HOSTS=127.0.0.1

##### 4. Создать виртуальное окружение

    python -m venv venv

##### 5. Запустить виртуальное окружение

    source venv/bin/activate

##### 7. Установить зависимости

    pip install -r requirements.txt

##### 8. Применить миграции

    python manage.py migrate

##### 9. Создать суперпользователя

    python manage.py createsuperuser

##### 10. Загрузить данные

    python manage.py load_place --url http://адрес/файла.json

Пример файла json:

    {
        "title": "Антикафе Bizone",
        "imgs": [
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg"
        ],
        "description_short": "Настольные и компьютерные игры...",
        "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей...",
        "coordinates": {
            "lng": "37.50169",
            "lat": "55.816591"
        }
    }

##### 11. Запустить приложение

    python manage.py runserver
