import os
import django
import random
from datetime import datetime, timedelta
from faker import Faker
from django.core.files.base import ContentFile

# ===================== Настройка Django =====================
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practic_2.settings')
django.setup()

from apps.projects.models import Project, ProjectFile
from apps.tasks.models import Task, Tag, ProjectStatus, ProjectPriority
from django.contrib.auth.models import User

fake = Faker()

# ===================== Пользователи =====================
user, created = User.objects.get_or_create(username='testuser')
if created:
    user.set_password('password123')
    user.save()

# ===================== Теги =====================
tags_objs = []
for _ in range(10):
    tag_name = fake.unique.word().capitalize()
    tag, _ = Tag.objects.get_or_create(name=tag_name)
    tags_objs.append(tag)

# ===================== Проекты и файлы =====================
projects_objs = []
media_root = os.path.join(os.getcwd(), 'media', 'projects')

for _ in range(5):
    project_name = fake.unique.company().replace(" ", "_")
    project_description = fake.text(max_nb_chars=200)

    # Создаем проект
    project, _ = Project.objects.get_or_create(
        name=project_name,
        defaults={'description': project_description}
    )

    # Создаем папку для проекта
    project_folder = os.path.join(media_root, project_name)
    os.makedirs(project_folder, exist_ok=True)

    # Создаем несколько файлов проекта
    files_objs = []
    for i in range(random.randint(1, 5)):
        file_name = f'{fake.word()}_{i}.txt'
        file_content = fake.text(max_nb_chars=500)
        file_path = os.path.join(project_folder, file_name)

        with open(file_path, 'w') as f:
            f.write(file_content)

        # Сохраняем в базу
        project_file = ProjectFile.objects.create(
            name=file_name,
            file=f'projects/{project_name}/{file_name}'
        )
        files_objs.append(project_file)

    project.files.set(files_objs)
    projects_objs.append(project)

# ===================== Задачи =====================
for _ in range(20):
    project = random.choice(projects_objs)
    task_title = fake.unique.sentence(nb_words=4)
    task_description = fake.text(max_nb_chars=150)
    task_status = random.choice([s.value for s in ProjectStatus])
    task_priority = random.choice([p.value for p in ProjectPriority])
    task_due = datetime.now() + timedelta(days=random.randint(1, 60))

    task = Task.objects.create(
        title=task_title,
        description=task_description,
        status=task_status,
        priority=task_priority,
        project=project,
        due_date=task_due,
        assigned=user
    )
    task.tags.set(random.sample(tags_objs, k=random.randint(1, 3)))

print("✅ Database seeded successfully with projects, files, and tasks!")
