# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
a = input("Введите результаты пробежки первого дня в км ")
b = input("Введите общий желаемый результат в км ")
day = 1
if int(a) > int(b):
    print (day)
    while int(a) < int(b):
        a = int(a) + int(a)/10
        day += 1
print(f"Вы достигнете требуемых показателей на %.d день" % day)

