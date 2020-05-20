# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

int = 3
float = 1.6
str = "Hello, world"
list = ['b', '6']
tuple = ('a', '2')
dict = {'world': 'Earth', 'Universe': 'planet'}

main_list = [int, float, str, list, tuple, dict]
for i in main_list:
    print(f'{i} is {type(i)}')