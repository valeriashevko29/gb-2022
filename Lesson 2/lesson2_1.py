# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [4, 'hello', 4.05, 5+7j, True, None, [1, 2, 3], (1, 2, 3), {'key1' : 5}]
for el in my_list:
    print(type(el))

