# Onlineshop
Проект создавался в рамках обучения. Полностью готов.

### Используемые технологи:
- Python 3.10
- Django 4.0.4
- PostgreSQL 14.5
- Docker 20.10.12

###  Функционал:
- Регистрация пользователя с автоматическим созданием профиля
- Реализована фильтрация по параметрам товара
- Добавление товара в корзину, создание и оформление заказа
- Добавление товара в избранное
- Отправка уведомлений при старте скидок и о доступности товара

## Установка
Склонируйте репозиторий <br>
- ```git clone https://github.com/paragonov/onlineshop```

<br>

Создайте файл .env.dev и запишите туда следующее  <br>
- ```python

  SECRET_KEY="ваш ключ"
  DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
  SQL_ENGINE=django.db.backends.postgresql
  SQL_DATABASE="название вашей бд"
  SQL_USER="логин пользователя вашей бд"
  SQL_PASSWORD="пароль пользователя вашей бд"
  SQL_HOST=db
  SQL_PORT=5432

  ```
<br>

Создайте образ docker <br>
- ```docker-compose build```

<br>

Запустите контейнеры <br>
- ```docker-compose up```

<br>

Перейдите на ```localhost:8000```
