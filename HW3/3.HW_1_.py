def my_func (x:float, y:float) -> float:
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"
print(my_func(input("Enter x = ")), (input("Enter y = ")))