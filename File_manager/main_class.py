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
        except OSError:
            print("Директория уже существует!")

    def rm_dir(self, name):
        """
        Удаление папки по имени
        """
        try:
            os.rmdir(name)
            print(f"Папка {name} удалена")
        except OSError:
            print("Директории не существует!")

    def moving_dir(self, name):
        """
        Переход между папками
        """
        try:
            os.chdir(name)
        except OSError:
            print("Директории не существует!")

    def new_file(self, name):
        """
        Создание пустых файлов с указанием имени
        """
        files = os.listdir(os.getcwd())
        if (name in files):
            print("Файл существует!")
            return 0
        with open(name, "w", encoding='utf-8') as file:
            pass

    def redirection(self, name):
        """
        Запись текста в файл
        """
        files = os.listdir(os.getcwd())
        if (name not in files):
            print("Файла не существует!")
            return 0
        with open(name, "a", encoding='utf-8') as file:
            text = str(input("Введите текст, который хотите добавить в файл: "))
            file.write(text)


    def my_cat(self, name):
        """
        Просмотр содержимого файла
        """
        files = os.listdir(os.getcwd())
        if (name not in files):
            print("Файла не существует!")
            return 0
        with open(name, "r", encoding='utf-8') as file:
            text = file.read()
            print(text)

    def rm_file(self, name):
        """
        Удаление файлов по имени
        """
        try:
            os.remove(name)
            print("Файл", name, "удален!")
        except FileNotFoundError:
            print("Файл не найден!")

    def copy_file(self, file_name, finish_path):
        """
        Копирование файлов из одной папки в другую
        """
        try:
            shutil.copy(file_name, finish_path)
            print(f"Файл {file_name} скопирован в {finish_path}!")
        except FileNotFoundError:
            print("Файл не найден!")

    def move_file(self, file_name, finish_path):
        """
        Перемещение файлов
        """
        try:
            shutil.move(file_name, finish_path)
            print(f"Файл {file_name} перемещен в {finish_path}")
        except (FileNotFoundError, shutil.Error):
            print("Файл не найден!")

    def rename_file(self, file_name, finish_name):
        """
        Переименование файлов
        """
        try:
            os.rename(file_name, finish_name)
            print(f"Файл {file_name} переименован в {finish_name}")
        except FileNotFoundError:
            print("Файл не найден!")

    def get_address(self):
        return os.getcwd()