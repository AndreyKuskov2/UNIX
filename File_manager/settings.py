import os

class Settings(object):
    """
    Класс с настройками
    """
    def __init__(self, path):
        os.chdir(path)
        