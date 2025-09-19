import os
import sys
import traceback
from calendar import weekday
from pathlib import Path
# from django.contrib.auth.models import User
from django.utils import timezone
import random



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practic_2.settings')
os.environ.setdefault('SECRET_KEY_DJANGO', 'dev-secret-key-for-local')

try:
    import django
    django.setup()
except Exception:
    print("Django not installed")
    traceback.print_exc()
    sys.exit(1)

from project.models import Tag, Project, ProjectFile, Task


# def create_tags():
#     tags_list =  [Tag(name='Backend'), Tag(name='Frontend'), Tag(name='Q&A'), Tag(name='Design'), Tag(name='DevOPS')]
#
#     # for tag in tags_list:
#     #     tag.save()
#
#     Tag.objects.bulk_create(tags_list)
#
#
# def create_projects():
#     list_project = [Project(name='Python',
#                             description='THIS IS A FIRST PROJECT'),
#                     Project(name='Django',
#                             description='THIS IS A TWO PROJECT')
#     ]
#
#     Project.objects.bulk_create(list_project)
#
# def create_files():
#     list_files = [ProjectFile(name='THE FIRST FILE', file='projects/first_file.txt'),
#                   ProjectFile(name='THE SECOND FILE', file='projects/second_file.pdf'),
#                   ProjectFile(name='THE THIRD FILE', file='projects/third_file.doc')
#                     ]
#
#     ProjectFile.objects.bulk_create(list_files)
#
# def create_user():
#     user_list =[User(username='backend_dev',password='sd7f6g5fsfd', email='backend.dev@gmail.com'),
#                  User(username='frontend_dev',password='sd7f6g5fsfd', email='frontend.dev@gmail.com'),
#                 User(username='designer', password='sd7f6g5fsfd', email='omg.designer@icloud.com'),
#                 User(username='devops', password='sd7f6g5fsfd',email='devops.3000@icloud.com'),
#                 User(username='qa_dev', password='sd7f6g5fsfd',email='qa.doesntmetter@gmail.com')
#                 ]
#
#     User.objects.bulk_create(user_list)
#
# def create_task():
#     project1 = Project.objects.get(name='Django')
#     project2 = Project.objects.get(name='Python')
#
#     user1 = User.objects.get(username='backend_dev')
#     user2 = User.objects.get(username='frontend_dev')
#     user3 = User.objects.get(username='designer')
#     user4 = User.objects.get(username='devops')
#     user5 = User.objects.get(username='qa_dev')
#
#     task_list = [Task(title='Task_1', priority='MEDIUM', project=project1, assigned=user1, due_date=timezone.now()),
#                  Task(title='Task_2', priority='MEDIUM', project=project1, assigned=user2, due_date=timezone.now()),
#                  Task(title='Task_3', priority='MEDIUM', project=project2, assigned=user1, due_date=timezone.now()),
#                  Task(title='Task_4', priority='MEDIUM', project=project2, assigned=user2, due_date=timezone.now())]
#
#     Task.objects.bulk_create(task_list)
#
# def add_tags():
#     tags = Tag.objects.all()
#     for task in Task.objects.all():
#         task.tags.add(random.choice(tags))

# Задание 7
"""
Получение тегов
1. Импортируйте модели тегов Tag.
2. Напишите запрос, который позволит получить список всех тегов.
3. Выведите имя каждого тега.
4. Получите самый первый тег.
5. Получите самый последний тег.
6. Получите кол-во всех тегов.
"""

# last_tag = Tag.objects.last()
# last_tag.title
# 'DevOPS'
# first_tag = Tag.objects.first()
# first_tag.title
# 'AAA'
# count_of_tags = Tag.objects.count()
# count_of_tags
# 7

# Задание 8
"""
Проверка существования тега с именем
1. Напишите запрос, который будет искать тэг по определённому имени
2. Проверьте наличие такого тега методом, который выдаёт True или False на наличие объекта.
"""

# from project.models import Tag
# tag_exists = Tag.objects.filter(title='Backend').exists()
# tag_exists
# True
# tag_exists_1 = Tag.objects.filter(title='Backen').exists()
# tag_exists_1
# False

# Задание 9
"""
Фильтрация тегов по имени
1. Напишите запрос, который позволит получить теги, у которых в имени будет совпадение по
переданной строке, например: “...Tagˮ
2. Выведите имена всех этих тегов.
"""

# from project.models import Tag
# tags_name = Tag.objects.filter(title__icontains='end')
# tags_name
# <QuerySet [<Tag: Backend .>, <Tag: Frontend .>]>

# Задание 10
"""
Фильтрация проектов по дате создания
1. Импортируйте модуль datetime и модель Project.
2. Создайте объект даты, по которой нужно сделать поиск.
3. Напишите запрос, который позволит получить список проектов, которые равны или старше
переданной даты создания.
4. Выведите имена таких проектов
"""
# from django.utils import timezone
# x = timezone.datetime(2023, 2, 3).astimezone()
# from project.models import Project
# y = Project.objects.filter(created_at__gt=x)
# y
# <QuerySet [<Project: Project_2 от 2025-09-10.>, <Project: Project_1 от 2025-09-10.>]>

# Задание 11
"""
Использование Q класса для комбинированных условий
1. Импортируйте модель Project.
2. Напишите запрос, который позволит получить необходимые проекты:
○ Реализуйте фильтрацию, которая будет проходить два условия:
■ Проекты, равные или больше указанной даты
■ Проекты, у которых в имени есть строка ‘TIʼ
3. Выведите имена таких проектов.
"""
# from project.models import Project
# from django.db import Q
# from django.db.models import Q
# from django.utils import timezone
# x = timezone.datetime(2023, 2, 3).astimezone()
# y = Project.objects.filter(Q(created_at__gt=x) & Q(title__icontains='pr'))
# y
# <QuerySet [<Project: Project_2 от 2025-09-10.>, <Project: Project_1 от 2025-09-10.>]>
# for i in y: print(i.title)
# Project_2
# Project_1

# Задание 12
"""
Получение списка всех файлов для проекта
1. Напишите запрос, который позволит получить список всех файлов, которые привязаны к
конкретному проекту. Поиск произведите по имени проекта.
2. Выведите только пути к каждому файлу
"""
# related_name="projects" используем
# files = ProjectFile.objects.filter(projects__title__icontains='pr')
# files
# <QuerySet [<ProjectFile: name1,/media/projects/project1/1.txt>, <ProjectFile: name2,/media/projects/project2/2.txt>, <ProjectFile: name1,/media/projects/project1/1.txt>, <ProjectFile: name2,/media/projects/project2/2.txt>]>

# 2 способ
# for item in x:
#     print(item.title)
#     for file in item.files.all():
#         print(file)
#     print('-'*20)

# Задание 13
"""
Фильтрация задач по статусу и приоритету
1. Напишите запрос, который поможет получить только те задачи, у которых:
○ Статус “newˮ
○ Приоритетность “Urgentˮ
2. Выведите информацию по каждой такой задаче:
○ Название
○ Статус
○ Приоритетность
○ Дата, когда задача должна быть сдана
○ Email сотрудника, за которым закреплена эта задача
"""

# tasks = Task.objects.filter(status='New', priority='MEDIUM')
# tasks
# <QuerySet [<Task: Task_1 от 2025-09-11 07:41:42.876125+00:00 для проекта Project_1 от 2025-09-10..Статус New. Выполняет Backend.>, <Task: Task_2 от 2025-09-11 07:41:42.877129+00:00 для проекта Project_1 от 2025-09-10..Статус New. Выполняет Frontend.>, <Task: Task_3 от 2025-09-11 07:41:42.877129+00:00 для проекта Project_2 от 2025-09-10..Статус New. Выполняет Backend.>, <Task: Task_4 от 2025-09-11 07:41:42.877129+00:00 для проекта Project_2 от 2025-09-10..Статус New. Выполняет Frontend.>]>
# for item in tasks:
#     print("=" * 50)
#     print(item.title)
#     print(item.status)
#     print(item.priority)
#     print(item.due_date)
#     print(item.assigned.email)
#     print("=" * 50)

# Задание 14
"""
Обновление статуса задачи
1. Напишите запрос, который поможет получить конкретную задачу
2. Обратитесь к полю статуса и обновите его на новое значение, например “pendingˮ. Сделайте это
через метод update().
"""

# from project.models import Task
# update = Task.objects.filter(title='Task_1')
#from project.models import StatusProject
# update.update(status=StatusProject.PENDING)


# Задание 15
"""
Получение задач через комбинацию условий
1. Напишите запрос, который будет содержать в себе прохождение одной из комбинаций:
○ статус и приоритетность
○ прохождение несовпадения по тегу
2. Выведите название этих задач, проект и email разработчиков.
"""

# from project.models import Task
# from django.db.models import Q
# from project.models import StatusProject
# from project.models import PriorityProject
# x = Task.objects.filter((Q(status=StatusProject.PENDING) & Q(priority=PriorityProject.MEDIUM)) | ~Q(tags__title='Q&A'))
# for task in x:
#     print("_" * 50)
#     print(task.title)
#     print(task.project.title)
#     print(task.assigned.email)
#     print("_" * 50)

# Задание 16
"""
Обновление приоритета задач
1. Импортируйте модель Task.
2. Импортируйте F класс.
3. Обновите приоритет задач, которые должны быть выполнены в следующем месяце, на "Extra".
Используйте F класс.
"""

# from django.db.models import F
# from project.models import Task
# from project.models import PriorityProject
# Task.objects.filter(due_date__month=F('created_at__month') + 1).update(priority=PriorityProject.VERY_HIGH)

# Задание 17
"""
Увеличение даты выполнения всех задач на неделю
1. Импортируйте модуль timedelta из библиотеки datetime.
2. Импортируйте модель Task.
3. Обновите все объекты задач по полю due_date на + 1 неделю. Используйте F класс.
"""

# from project.models import Task
# from django.db.models import F
# from datetime import timedelta
# Task.objects.update(due_date=F('due_date') + timedelta(weeks=1))

# Задание 18
"""
Фильтрация задач, у которых нет прикрепленного разработчика
1. Импортируйте модель Task.
2. Напишите запрос, который поможет профильтровать по lookups полю те задачи, у которых нет
назначенного разработчика.
3. Выведите название таких задач и название проекта для этих задач.
"""

# from project.models import Task
# from datetime import timedelta
# x = Task.objects.filter(assigned__isnull=True)
# for item in x:
#     print("=" * 50)
#     print(item.title)
#     print(item.project.title)
#     print("=" * 50)

# Задание 19
"""
Получение задач
Необходимо получить все задачи, связанные с тегами и содержащими определённое ключевое слово.
1. Импортируйте модель Task.
2. Напишите запрос, который поможет отфильтровать задачи через конкретный тэг.
○ Запрос должен быть написан с использованием lookups полей
○ Запрос должен начинаться с модели Task, через эту модель нужно получить доступ к
конкретному тэгу.
3. Выведите информацию по каждой задаче:
○ Имя задачи
○ Статус задачи
○ Приоритет задачи
○ Имя проекта этой задачи
"""

# from project.models import Task
# x = Task.objects.filter(tags__title__icontains='DevOPS')
# for item in x:
#     print("=" * 50)
#     print(item.title)
#     print(item.status)
#     print(item.priority)
#     print(item.project.title)
#     print("=" * 50)

# Задание 20
"""
Получение проектов
Необходимо получить все проекты, связанные с файлами, созданными в определенный период (последняя
неделя).
1. Импортируйте модели Project, ProjectFile.
2. Создайте переменную с датой периода создания файлов (от текущего дня 7 дней)
3. Напишите первый запрос, который поможет получить те файлы, которые должны быть больше, или
равны полученной дате по полю создания этого файла
4. Напишите запрос, который поможет получить только те проекты, у которых есть те файлы, что мы
получили предыдущим запросом.
5. Выведите информацию об этих проектах: имя проекта и дата создания
"""

# from project.models import Project,ProjectFile
# from django.utils import timezone
# from datetime import timedelta
# x = timezone.now() - timedelta(days=7)
# f =  ProjectFile.objects.filter(created_at__gte=x)
# p = Project.objects.filter(files__in=f).distinct()


from django.db.models import Count, Avg
from django.db.models.functions import ExtractWeekDay
from project.models import Project, ProjectFile


# projects = Project.objects.filter(created__month=timezone.now().month)
# if projects:
#     for proj in projects:
#         print("=" * 50)
#         print(proj.name)
#         print(proj.created)
# else:
#     print("EMPTY DATA")

# ============== 2 ==========================

# project_file = ProjectFile.objects.annotate(
#     weekday=ExtractWeekDay('created'),
# ).filter(weekday=2)
#
# if project_file:
#     for item in project_file:
#         print(f"{item.name}")
#         print(f"{item.file}")

# =============== 3 ==============================
# count_projects = Project.objects.all().count()
#
# print(count_projects)

# ================= 4 =============================

# projects = Project.objects.annotate(file_count=Count('files'))
# for project in projects:
#     print(f"{project.name}, {project.file_count}")
#
# files = ProjectFile.objects.annotate(project_count=Count('projects'))
# for f in files:
#     print(f"{f.name}, {f.project_count}")

# =================== 5 ==============================
# projects = Project.objects.annotate(file_count=Count('files'))
# avg_files = projects.aggregate(avg_file_count=Avg('file_count'))
#
# for project in projects:
#     print(f"Проект: {project.name}, файлов: {project.file_count}")
#
# print(f"AVG файлов на проект: {avg_files['avg_file_count']}")

# =================== 6 =====================================
# from django.contrib.auth.models import User
# users_with_task_count = User.objects.annotate(
#     count_of_tasks=Count('assigned_tasks')
# ).values('username', 'count_of_tasks')
#
# for user in users_with_task_count:
#     print(f"{user['username']}: {user['count_of_tasks']} задач")

# ======================== 7 =================================

# tasks = Task.objects.order_by('priority', 'due_date').values('title', 'priority', 'due_date')
#
# for task in tasks:
#     print(f" {task['title']}, {task['priority']}, {task['due_date']}")

# ====================== 8 ====================================
# from django.contrib.auth.models import User
#
# users_with_task_count = User.objects.annotate(
#     count_of_tasks=Count('assigned_tasks')
# ).values('username', 'count_of_tasks').order_by('-count_of_tasks')
#
# for user in users_with_task_count:
#     print(f"{user['username']}: {user['count_of_tasks']} задач")

# ===================== 9 ============================
# from django.core.paginator import Paginator
#
# tasks = Task.objects.select_related('assigned').all()
# paginator = Paginator(tasks, 10)
#
# page_number = 1
# page_obj = paginator.get_page(page_number)
#
# for task in page_obj:
#     username = task.assigned.username if task.assigned else "Done"
#     print(f" {task.title},  {task.status}, {task.priority}, Разработчик: {username}")

# ======================= 10 ==============================









