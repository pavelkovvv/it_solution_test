# it_solution_test

## Описание проекта

Проект позволяет сгенерировать и скачать видео с бегущей строкой предварительно указав параметры данного видео.

В проекте реализованы следующие функции:

- Указание параметров видео;
- Скачивание видео по запросу;
- Возможность посмотреть историю запросов пользователей;
- Реализована пагинация в истории запросов;
- Сайт имеет свой собственный домен (runningline.hopto.org);
- К сайту добавлен SSL-сертификат;

## Системные требования

- Python 3.9+
- Linux, Windows, MacOS, BSD


## Технологии

- Python 3.9
- Django 4.2
- SQLite3


## Установка проекта и его запуск

1. Клонировать репозиторий и перейти в него:
```
git clone git@github.com:pavelkovvv/it_solution_test.git
```

2. Создать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

3. Обновить pip и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:
```
python manage.py migrate
```

5. Запустить проект:
```
python manage.py runserver
```
