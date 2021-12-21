# API и его тестирование

## Чтобы начать работу, необходимо получить ключ аутенфикации пользователя с помощью GET запроса:

![image](./pictures/key.png)

## Добавим новое животное без фотографии:

![image](./pictures/new_pet.png)
![image](./pictures/new_pet_code.png)

## Просмотрим список, добавленных мною животных: 

![image](./pictures/pet_list.png)

## Добавим фотографию к добавленному животному:

![image](./pictures/add_photo.png)

## Получим информацию по всем животным:

![image](./pictures/info.png)

## Добавим новое животное с фотографией:

![image](./pictures/new_pet_with_pic.png)
![image](./pictures/new_pet_with_pic_code.png)

# Тестирование API

Запустим тест

![image](./pictures/test.png)

В ходе выполнения тестов мы получаем ожидаемую ошибку.

В коде тестов использовалась как параметризация, так и фикстура:

Фикстура:

![image](./pictures/fixture.png)

Параметризация

![image](./pictures/param.png)