import os
from main_class import FileManager
from time import sleep

def get_instructions():
    print("nd - Создание папки (с указанием имени)")
    print("rmd - Удаление папки по имени")
    print("md - Переход между папками")
    print("nf - Создание пустых файлов с указанием имени")
    print("rd - Запись текста в файл")
    print("mc - Просмотр содержимого файла")
    print("rmf - Удаление файлов по имени")
    print("cf - Копирование файлов из одной папки в другую")
    print("mf - Перемещение файлов")
    print("rf - Переименование файлов")

def main():
    flag = 0

    while True:
        if(flag == 0):
            #path = str(input("Укажите путь до рабочей директории: "))
            path = "C:/Users/Andrey/Programs/UNIX/File_manager"
            file_manager = FileManager(path)
            flag = 1
        print("Рабочая директория:", os.getcwd())
        x = str(input("Введите команду (help для вызова инструкции): "))
        if(x == "nd"):
            x = str(input("Введите название новой папки: "))
            file_manager.new_dir(x)
            continue
        if(x == "rmd"):
            x = str(input("Введите название папки для удаления: "))
            file_manager.rm_dir(x)
            continue
        if(x == "md"):
            x = str(input("Введите имя директории, в которую хотите перейти: "))
            file_manager.moving_dir(x)
            continue
        if(x == "nf"):
            x = str(input("Введите название нового файла: "))
            file_manager.new_file(x)
            continue
        if(x == "rd"):
            x = str(input("Введите название файла, в который хотите записать: "))
            file_manager.redirection(x)
            continue
        if(x == "mc"):
            x = str(input("Введите название файла для просмотра: "))
            file_manager.my_cat(x)
            continue
        if(x == "rmf"):
            x = str(input("Введите название файла для удаления: "))
            file_manager.rm_file(x)
            continue
        if(x == "cf"):
            x = str(input("Введите имя файла, который хотите скопировать: "))
            y = str(input("Укажите конечный путь, куда вы хотите скопировать файл: "))
            file_manager.copy_file(x, y)
            continue
        if(x == "mf"):
            x = str(input("Введите имя файла, который хотите переместить: "))
            y = str(input("Укажите конечный путь, куда вы хотите переместить файл: "))
            file_manager.move_file(x, y)
            continue
        if(x == "rf"):
            x = str(input("Введите имя файла, который хотите переименовать: "))
            y = str(input("Укажите новое имя файла: "))
            file_manager.rename_file(x, y)
            continue
        if(x == "help"):
            get_instructions()  
        if(x == "exit"):
            break      

if __name__ == "__main__":
    main()