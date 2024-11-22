Cars Control Project
====================

Описание
--------

**Cars Control Project** — это веб-приложение для управления автомобилями и комментариями к ним. Пользователи могут добавлять, редактировать и удалять свои автомобили, оставлять комментарии к автомобилям, а также просматривать автомобили других пользователей. Приложение реализовано с использованием Django и Django REST Framework.

* * *

Установка и запуск
------------------

### Требования

*   Python 3.10+
*   pip (менеджер пакетов Python)
*   Виртуальная среда (например, `venv`)

### Установка

1.  Склонируйте репозиторий:
    
        git clone <ссылка на репозиторий>
        cd cars_control
    
2.  Создайте и активируйте виртуальную среду:
    
        python -m venv venv
        source venv/bin/activate    # Linux/Mac
        venv\Scripts\activate       # Windows
    
3.  Установите зависимости:
    
        pip install -r requirements.txt
    

* * *

### Настройка

1.  Выполните миграции базы данных:
    
        python manage.py makemigrations
        python manage.py migrate
    
2.  Создайте суперпользователя для доступа к административной панели:
    
        python manage.py createsuperuser
    
3.  Запустите сервер разработки:
    
        python manage.py runserver
    

* * *

Использование
-------------

### API

#### Список конечных точек

*   **Машины:**
    *   `GET /api/cars/` — Получить список всех машин.
    *   `GET /api/cars/<id>/` — Получить информацию о конкретной машине.
    *   `POST /api/cars/` — Добавить новую машину (только для авторизованных пользователей).
    *   `PUT /api/cars/<id>/` — Обновить информацию о машине (только для владельца).
    *   `DELETE /api/cars/<id>/` — Удалить машину (только для владельца).
*   **Комментарии:**
    *   `GET /api/cars/<id>/comments/` — Получить список комментариев к машине.
    *   `POST /api/cars/<id>/comments/` — Добавить комментарий к машине (только для авторизованных пользователей).

#### Пример запроса с использованием `curl`:

    # Получение списка машин
    curl -X GET http://127.0.0.1:8000/api/cars/
    
    # Добавление новой машины (нужно предварительно авторизоваться http://127.0.0.1:8000/login)
    curl -X POST -H "Content-Type: application/json" \
         -d '{"make": "Toyota", "model": "Camry", "year": 2021, "description": "Compact sedan"}' \
         http://127.0.0.1:8000/api/cars/


* * *

### Интерфейс

1.  Перейдите на главную страницу приложения: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2.  Авторизуйтесь или зарегистрируйтесь, чтобы управлять своими автомобилями.
3.  Используйте профиль для добавления, редактирования и удаления своих автомобилей.
4.  Просматривайте автомобили и оставляйте комментарии через главный интерфейс.

* * *

Безопасность
------------

*   Все операции по добавлению, редактированию и удалению автомобилей доступны только для зарегистрированных пользователей.
*   Комментарии можно оставлять только после авторизации.
*   Пользователь может редактировать и удалять только свои автомобили.
