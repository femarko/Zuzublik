## Запуск
### Подготовка: токен и файл `.env`
- создать новый телеграм-бот и получить токен: [@BotFather](https://t.me/BotFather)
- перейти в директорию, куда планируется поместить приложение, и находясь в этой 
- директории, клонировать репозиторий и перейти в директорию ```Zuzublik```:
```bash
$ git clone git@github.com:femarko/Zuzublik.git
$ cd Zuzublik
```

### Запуск в докер-контейнере
```bash
$ git clone git@github.com:femarko/Zuzublik.git
$ cd Zuzublik
$ docker build . --tag=zuzublik_bot
$ docker run --env-file .env zuzublik_bot:latest
```
### Запуск локально
```bash
$ git clone git@github.com:femarko/Zuzublik.git
$ cd Zuzublik
$ python3 venv venv_zuzublik_bot
$ source venv_zuzublik_bot/bin/activate  # Linux
$ source venv_zuzublik_bot/Scripts/activate  # Windows
$ python3 -m app.dp.create_db
$ python3 -m app.entrypoints.bot
```
---
## Структура приложения и комментарии
### Структура приложения

### Комментарии
- запуск скрипта, который требовалось написать:
```bash
$ python3 -m task_7.main
```
Отсутствие в командной строке трассировки исключений (AssertionError и других)
говорит об успешном выполнении скрипта с тестовыми данными.
