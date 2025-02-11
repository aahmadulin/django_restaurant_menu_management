# django_restaurant_menu_management

Проект представляет собой REST API для управления блюдами и категориями блюд в ресторане (создание, управление, публикация). Проект разработан на Django и Django REST Framework.

## Функции
-Получение списка категорий блюд.

-Получение списка блюд в каждой категории.

-Фильтрация блюд по полю is_publish=True.

-Исключение категорий, в которых нет опубликованных блюд.

## Как установить?
Перво-наперво, создайте папку под проект.

1) Клонируйте в папку репозиторий: git clone https://github.com/aahmadulin/django_restaurant_menu_management
2) Перейдите в папку проекта: cd django_restaurant_menu_management/subfolderutf
3) Создайте виртуальное окружение: python -m venv .venv
4) Активируйте виртуальное окружение: .venv\Scripts\activate (если у вас Windows), source .venv/bin/activate (если у вас macOS/Linux)
5) Установите зависимости из requirements.txt: pip install -r requirements.txt
6) Примените миграции: python manage.py migrate
7) Можете создать суперюзера (чтобы создавать категории и блюда): python manage.py createsuperuser (далее вам нужно будет ввести юзернейм, почту и пароль. по юзернейму вы сможете войти в админку)
8) Запустите сервер: python manage.py runserver

## Что делать дальше?
1) Перейдите на /admin/ (http://127.0.0.1:8000/admin/). Здесь вы сможете создать категорию блюда и само блюдо.
2) Перейдите на /api/v1/foods/ (http://127.0.0.1:8000/api/v1/foods/). Здесь вы сможете получить JSON опубликованных блюд
3) Далее вы получите список блюд (если они опубликованы). Примерно такой:
4) Чтобы остановить работу сервера, нажмите Ctrl + C

```
[
    {
        "id": 2,
        "name_ru": "Выпечка",
        "name_en": null,
        "name_ch": null,
        "order_id": 20,
        "foods": [
            {
                "internal_code": 4,
                "code": 400,
                "name_ru": "Пирожок с ничем",
                "description_ru": "Пирожок с ничем",
                "description_en": null,
                "description_ch": null,
                "is_vegan": true,
                "is_special": false,
                "cost": "50.00",
                "additional": []
            }
        ]
    },
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": "Drinks",
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 100,
                "code": 1,
                "name_ru": "Чайочек",
                "description_ru": "Чайочек пакетированный",
                "description_en": "Tea bags",
                "description_ch": null,
                "is_vegan": true,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            },
            {
                "internal_code": 2,
                "code": 200,
                "name_ru": "Кола",
                "description_ru": "Кола",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            },
            {
                "internal_code": 3,
                "code": 300,
                "name_ru": "Спрайт",
                "description_ru": "Спрайт",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            }
        ]
    }
]
```

Скриншоты с примерами:
![image_2025-02-11_23-38-59](https://github.com/user-attachments/assets/3548b76c-0b3b-4e8a-977c-4e27e3fc46e3)
![image_2025-02-11_23-39-27](https://github.com/user-attachments/assets/2578a109-051d-4147-be04-1f7e11c67c9e)
