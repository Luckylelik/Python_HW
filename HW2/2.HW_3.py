# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = input("Введите месяц по номеру ")
if int(month) ==1 or int(month) == 12 or int(month) == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif int(month) == 3 or int(month) == 4 or int(month) == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif int(month) == 6 or int(month) == 7 or int(month) == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif int(month) == 9 or int(month) == 10 or int(month) == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")