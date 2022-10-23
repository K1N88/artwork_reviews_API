# YaMDb

## Содержание
- [Описание проекта](#Описание-проекта)
- [Технологический стек](#Технологический-стек)
- [Запуск проекта](#Запуск-проекта)
- [Примеры работы с проектом](#Примеры-работы-с-проектом)
- [Инструкции для накачки базы из CSV-файлов](#Инструкции-для-накачки-базы-из-CSV-файлов)
- [Над проектом работали](#Над-проектом-работали)

### Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в
YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». 
Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» 
и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» 
и вторая сюита Баха. Список категорий может быть расширен (например, можно 
добавить категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен жанр из списка предустановленных (например, 
«Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые 
отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое 
число); из пользовательских оценок формируется усреднённая оценка произведения 
— рейтинг (целое число). На одно произведение пользователь может оставить 
только один отзыв.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные 
пользователи.

### Технологический стек:

- Python
- Django
- DjangoRestFramework
- JWT

### Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:aleksandr-miheichev/api_yamdb.git
```

Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

### Примеры работы с проектом:

Удобную веб-страницу со справочным меню, документацией для эндпоинтов и 
разрешённых методов, с примерами запросов, ответов и кода Вы сможете посмотреть 
по адресу:

[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


### Инструкции для накачки базы из CSV-файлов:

Для загрузки данных, получаемых вместе с проектом, из файлов csv в базу данных 
через Django ORM была написана собственная management-команда.

Увидеть её описание Вы сможете, открыв папку:
```
api_yamdb/api_yamdb
```
в терминале и далее введя команду:
```
python manage.py data_loading -h
```
Для выполнения процедуры загрузки в базу данных необходимо выполнить:
```
python manage.py data_loading
```
В случае успешного выполнения данной процедуры будет выведено сообщение в 
терминал:
```
Database successfully loaded into models!
```
При отсутствии csv файла с данными или его неправильного наименования будет 
выведена ошибка:
```
Sorry, the file "<название_файла>" does not exist.
```
При необходимости внести корректировки в данную management-команду Вы сможете 
найти её исполняющий файл в папке:
```
api_yamdb/api_yamdb/reviews/management/commands
```
### Над проектом работали:
- [Михеичев Александр](https://github.com/aleksandr-miheichev)
- [Назаров Константин](https://github.com/K1N88)
- [Тищенко Николай](https://github.com/NikolayTishenko)
