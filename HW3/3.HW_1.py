# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div (*user_inputs):
    try:
        user_input1 = input("Enter x = ")
        user_input2 = input("Enter y = ")
        x = abs(int(user_input1))
        y = abs(int(user_input2))
        result = x / y
    except ZeroDivisionError:
        return "y isn't be a zero"
    except ValueError:
        return "enter only number"
    return result
print(f'result {div()}')