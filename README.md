## Запуск
### Токен и файл `.env`
- создать новый телеграм-бот и получить токен: [@BotFather](https://t.me/BotFather)
- перейти в директорию, куда планируется поместить приложение
- находясь в этой директории:
  - клонировать репозиторий, содержащий ранее полученный токен:
    ```bas
    $ git clone git@github.com:femarko/Zuzublik.git
    ```

  - перейти в директорию ```Zuzublik``` и создать файл ```.env```, куда записать ранее
  полученный токен:
    ```bash
    $ cd Zuzublik
    $ cat > .env
    $ BOT_TOKEN=<your_bot_token>
    ```
  - нажать комбинацию клавиш `Ctrl` + `D`

### Запуск в докер-контейнере
```bash
$ cd Zuzublik
$ docker build . --tag=zuzublik_bot
$ docker run --env-file .env zuzublik_bot:latest
```
### Запуск локально
```bash
$ cd Zuzublik
$ python3 venv venv_zuzublik_bot
$ source venv_zuzublik_bot/bin/activate  # Linux
$ source venv_zuzublik_bot/Scripts/activate  # Windows
$ pip install -r requirements.txt
$ python3 -m app.dp.create_db
$ python3 -m app.entrypoints.bot
```
---
## Подход к реализации и структура приложения

### Подход к реализации:
- телеграм-бот является только одним из возможных интерфейсов 
приложения
- элементы приложения слабо связаны между собой, что позволяет "безболезненно" 
менять их, или дополнять новыми, например:
  - вместо ```Pydantic``` использовать другие
  библиотеки валидации
  - вместо ```SQLAlchemy``` использовать "сырой" SQL
  - вместо ```SQLite``` использовать ```PostgreSQL```
### Структура приложения:
  - [domain](https://github.com/femarko/Zuzublik/tree/main/app/domain) - предметная 
область:
    - [models.py](https://github.com/femarko/Zuzublik/blob/main/app/domain/models.py): 
класс ```Zuzublik``` и функция, создающая экземпляр этого класса
    - [errors.py](https://github.com/femarko/Zuzublik/blob/main/app/domain/errors.py): 
    кастомные классы исключений, использующиеся в приложении как часть бизнес-логики
  - [repository](https://github.com/femarko/Zuzublik/tree/main/app/repository): 
абстракция постоянного хранилища данных
  - [db](https://github.com/femarko/Zuzublik/tree/main/app/db) - пакет лоя базы данных:
    - [create_db.py](https://github.com/femarko/Zuzublik/blob/main/app/db/create_db.py): 
    скрипт создания базы данных
    - zuzu.db - файл базы данных SQLite (создается при выполнении скрипта создания БД)
  - [orm_tool](https://github.com/femarko/Zuzublik/tree/main/app/orm_tool) - пакет 
для object-relational mapper:
    - [sql_aclchemy_wrapper.py](https://github.com/femarko/Zuzublik/blob/main/app/orm_tool/sql_aclchemy_wrapper.py): 
все настройки для ```SQLAlchemy``` + мэппинг классов python из ```models.py``` с таблицами БД
  - [auxiliary_services](https://github.com/femarko/Zuzublik/tree/main/app/auxiliary_services) - 
все вспомогательные сервисы:
    - 