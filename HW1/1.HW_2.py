# Задача-2: Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time = input("Enter your local time in sec: ")
hours = int(time) // 3600
modulo = int(time) % 3600
minutes = modulo // 60
sec = modulo % 60
print(f"Now is {hours}:{minutes}:{sec} ")