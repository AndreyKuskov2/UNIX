from _pytest.nodes import File
import pytest
import os
from main_class import FileManager

path = "./"
a1 = FileManager(path)

def test_new_dir_pos():
	assert 1 == a1.new_dir("12")

def test_new_dir_neg():
	with pytest.raises(OSError) as error:
		a1.new_dir("home")
	assert "Директория уже существует!" == error.value.args[0]



def test_rm_dir_pos():
	assert 1 == a1.rm_dir("12")

def test_rm_dir_neg():
	with pytest.raises(OSError) as error:
		a1.rm_dir("qwerty")
	assert "Директории не существует!" == error.value.args[0]


def test_new_file_pos():
	assert 1 == a1.new_file("123.txt")

def test_new_file_neg():
	with pytest.raises(OSError) as error:
		a1.new_file("123.txt")
	assert "Файл существует!" == error.value.args[0]



def test_redirection_pos():
	a1.new_file("test_file")
	assert 1 == a1.redirection("test_file")

def test_redirection_neg():
	with pytest.raises(OSError) as error:
		a1.redirection("qwerty123")
	assert "Файла не существует!" == error.value.args[0]


def test_my_cat_pos():
	assert 1 == a1.my_cat("123.txt")

def test_my_cat_neg():
	with pytest.raises(OSError) as error:
		a1.my_cat("qwerty123")
	assert "Файла не существует!" == error.value.args[0]



def test_rm_file_pos():
	a1.new_file("andrey")
	assert 1 == a1.rm_file("andrey")

def test_rm_file_neg():
	with pytest.raises(FileNotFoundError) as error:
		a1.rm_file("qwerty123")
	assert "Файл не найден!" == error.value.args[0]



def test_copy_file_pos():
	a1.new_file("ggg")
	assert 1 == a1.copy_file("ggg", "home")

def test_copy_file_neg():
	with pytest.raises(FileNotFoundError) as error:
		a1.copy_file("qwerty123", "home")
	assert "Файл не найден!" == error.value.args[0]



def test_move_file_pos():
	a1.new_file("ppp")
	assert 1 == a1.move_file("ppp", "home")

def test_move_file_neg():
	with pytest.raises(FileNotFoundError) as error:
		a1.move_file("qwerty123", "home")
	assert "Файл не найден!" == error.value.args[0]



def test_rename_file_pos():
	assert 1 == a1.rename_file("123.txt", "asdsad")
	a1.rm_file("asdsad")
	a1.rm_file("ggg")
	a1.rm_file("test_file")

def test_rename_file_neg():
	with pytest.raises(FileNotFoundError) as error:
		a1.rename_file("qwerty123", "ytrewq")
	assert "Файл не найден!" == error.value.args[0]



def test_moving_dir_pos():
	assert 1 == a1.moving_dir("home")
	a1.rm_file("ggg")
	a1.rm_file("ppp")

def test_moving_dir_neg():
	with pytest.raises(OSError) as error:
		a1.moving_dir("qwerty")
	assert "Директории не существует!" == error.value.args[0]

if __name__ == "__main__":
	pytest.main()