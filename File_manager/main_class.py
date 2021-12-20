import os
import shutil
from settings import Settings

class FileManager(Settings):
    """
    Класс, реализующуй файловый менеджер.
    """
    def __init__(self, path):
        """
        Инициализация класса
        """
        super().__init__(path)

    def new_dir(self, name):
        """
        Создание папки (с указанием имени)
        """
        try:
            os.mkdir(name)
            print(f"Папка {name} создана")
            return 1
        except OSError:
            raise OSError("Директория уже существует!")

    def rm_dir(self, name):
        """
        Удаление папки по имени
        """
        try:
            os.rmdir(name)
            print(f"Папка {name} удалена")
            return 1
        except OSError:
            raise OSError("Директории не существует!")

    def moving_dir(self, name):
        """
        Переход между папками
        """
        try:
            os.chdir(name)
            return 1
        except OSError:
            raise OSError("Директории не существует!")

    def new_file(self, name):
        """
        Создание пустых файлов с указанием имени
        """
        files = os.listdir(os.getcwd())
        if (name in files):
            raise OSError("Файл существует!")
        with open(name, "w", encoding='utf-8') as file:
            pass
        return 1

    def redirection(self, name):
        """
        Запись текста в файл
        """
        files = os.listdir(os.getcwd())
        if (name not in files):
            raise OSError("Файла не существует!")
        with open(name, "a", encoding='utf-8') as file:
            text = str(input("Введите текст, который хотите добавить в файл: "))
            file.write(text)
        return 1

    def my_cat(self, name):
        """
        Просмотр содержимого файла
        """
        files = os.listdir(os.getcwd())
        if (name not in files):
            raise OSError("Файла не существует!")
        with open(name, "r", encoding='utf-8') as file:
            text = file.read()
            print(text)
        return 1

    def rm_file(self, name):
        """
        Удаление файлов по имени
        """
        try:
            os.remove(name)
            print("Файл", name, "удален!")
            return 1
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден!")

    def copy_file(self, file_name, finish_path):
        """
        Копирование файлов из одной папки в другую
        """
        try:
            shutil.copy(file_name, finish_path)
            print(f"Файл {file_name} скопирован в {finish_path}!")
            return 1
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден!")

    def move_file(self, file_name, finish_path):
        """
        Перемещение файлов
        """
        try:
            shutil.move(file_name, finish_path)
            print(f"Файл {file_name} перемещен в {finish_path}")
            return 1
        except (FileNotFoundError, shutil.Error):
            raise FileNotFoundError("Файл не найден!")

    def rename_file(self, file_name, finish_name):
        """
        Переименование файлов
        """
        try:
            os.rename(file_name, finish_name)
            print(f"Файл {file_name} переименован в {finish_name}")
            return 1
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден!")
            