import os
from django.core.exceptions import ValidationError


ALLOWED_EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.png', '.jpg', '.txt']
MAX_FILE_SIZE_MB = 2

def check_extension(filename: str) -> None:
    """
    проверяем расширение файлов
    """
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f"Extension '{ext}' is not allowed. Allowed: {ALLOWED_EXTENSIONS}")


def check_file_size(file) -> None:
    """
    Проверяет размер файла.
    """
    if file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise ValidationError(f"File size should not exceed {MAX_FILE_SIZE_MB} MB.")

def create_file_path(instance, filename: str) -> str:
    """
    генерирует путь для сохранения файла.
    """
    project_name = instance.project.name.replace(' ', '_')
    return f"projects/{project_name}/{filename}"

def save_file(file, path: str) -> None:
    """
    Сохраняет файл по указанному пути.
    """
    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
