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
## Структура приложения и комментарии
### Комментарии
Выбрана реализация, изолирующая 
```bash
$ python3 -m task_7.main
```
Отсутствие в командной строке трассировки исключений (AssertionError и других)
говорит об успешном выполнении скрипта с тестовыми данными.
