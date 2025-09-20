# 📌 Project Management System

Django-приложение для управления проектами и задачами.
Поддерживает статусы задач, приоритеты, теги и привязку к пользователям.

⭐ **Если проект понравился, ставьте звёзды на GitHub!**

---

## 🚀 Возможности

* 📁 Управление проектами (`Project`) и файлами проектов (`ProjectFile`)
* 📝 Управление задачами (`Task`) и тегами (`Tag`)
* 🔄 Статусы задач: `NEW`, `IN_PROGRESS`, `COMPLETED`, `CLOSED`, `PENDING`, `BLOCKED`
* ⚡ Приоритеты задач: `LOW`, `MEDIUM`, `HIGH`, `VERY_HIGH`, `CRITICAL`
* 👥 Привязка задач к проектам и пользователям
* 🕒 Даты создания, обновления, дедлайна и soft-delete
* 🛠 REST API через Django REST Framework

---

## 🛠 Технологии

* Python 3.11+
* Django 5.x
* Django REST Framework
* SQLite / PostgreSQL
* Django Admin

---

## 📂 Структура проекта

```
practic_2/
│── manage.py
│── apps/
│   ├── projects/
│   │    ├── models/
│   │    │    ├── project.py        # модель Project
│   │    │    └── project_file.py   # модель ProjectFile
│   │    ├── serializers/
│   │    │    ├── project.py        # сериализатор Project
│   │    │    └── project_file.py   # сериализатор ProjectFile
│   │    ├── admin.py
│   │    ├── apps.py
│   │    ├── view.py
│   │    ├── urls.py
│   │    ├── tests.py
│   │    └── __init__.py
│   ├── tasks/
│   │    ├── models/
│   │    │    ├── tasks.py          # модель Task
│   │    │    └── tags.py           # модель Tag
│   │    ├── serializers/
│   │    │    ├── tasks.py          # сериализатор Task
│   │    │    └── tags.py           # сериализатор Tag
│   │    ├── utils/
│   │    │    └── set_end_of_month.py          # функция calculate_end_of_month()
│   │    ├── choices/
│   │    │    ├── priority.py
│   │    │    └── statuses.py
│   │    ├── admin.py
│   │    ├── apps.py
│   │    ├── view.py
│   │    ├── urls.py
│   │    ├── tests.py
│   │    └── __init__.py
│   └── __init__.py

```

## ⚙️ Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/username/practic_2.git
cd practic_2

# 2. Создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Выполнить миграции
python manage.py makemigrations
python manage.py migrate

# 5. Создать суперпользователя
python manage.py createsuperuser

# 6. Запустить сервер
python manage.py runserver
```

---

## 🧩 Использование

* Панель администратора: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* Управление проектами и задачами через Django Admin
* Работа с API через сериализаторы (Django REST Framework)

---

## 📌 Полезные функции

В `apps/tasks/utils/set_end_of_month.py` есть функция:

```python
from apps.tasks.utils import calculate_end_of_month

calculate_end_of_month()
# → возвращает datetime с последним днём текущего месяца
```

---

## ✅ TODO

* 🔹 REST API для задач и проектов
* 🔹 Frontend для пользователей
* 🔹 Нотификации о дедлайнах
* 🔹 Тесты с pytest / Django TestCase

---
