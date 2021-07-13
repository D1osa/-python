my_argument_1 = int(input('Введите число 1: '))
my_argument_2 = int(input('Введите число 2: '))


def my_func(my_argument_1, my_argument_2):
    try:
         return my_argument_1 / my_argument_2
    except ZeroDivisionError:
         print('На ноль делить нельзя!')


print(my_func(my_argument_1, my_argument_2))
