import os
import uuid

from webapp.config import ALLOWED_IMAGE, MEDIA_FOLDER, UPLOAD_PATH

from wtforms import FileField

cls = 'Класс'


def is_extension_allowed(photo: FileField) -> bool:
    """Проверка на допустимое расширение картинки"""

    photo_name = photo.filename
    extension = photo_name.split('.')[-1]
    if extension in ALLOWED_IMAGE:
        return True
    else:
        return False


def save_files(photo: FileField) -> str:
    """
    Сохраниение загружамой картинки с возратом пути
    по которому сохранена картинка
    """

    photo_path = ''
    photo_name = photo.filename
    unique_filename = str(uuid.uuid4())
    extension = photo_name.split('.')[-1]
    photo_name_ext = f'{unique_filename}.{extension}'
    os.makedirs(UPLOAD_PATH, exist_ok=True)  # Проверяет есть ли папка, если нету создает
    photo.save(os.path.join(UPLOAD_PATH, photo_name_ext))
    photo_path = f"{MEDIA_FOLDER}/{photo_name_ext}"

    return photo_path
