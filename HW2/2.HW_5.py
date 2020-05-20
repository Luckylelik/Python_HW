# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# не получается
my_list = [5, 4, 2, 9, 4]
print(f"Рейтинг - {my_list}")
digit = input("Введите число (111 - выход) ")
while int(digit) != 111:
    for el in range(len(my_list)):
        if my_list[el] == int(digit):
            my_list.insert(el + 1, int(digit)
        elif my_list[0] < int(digit):
            my_list.insert(0, int(digit)
        elif my_list[-1] > int(digit):
            my_list.append(int(digit))
        elif my_list[el] > int(digit) and my_list[el + 1] < int(digit):
            my_list.insert(el + 1, int(digit)
    print(f"текущий список - {my_list}")
    digit = input("Введите число "))