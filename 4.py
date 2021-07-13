# с помощью оператора **

x = float(input('Введите действительное положительное число х: '))
y = int(input('Введите целое отрицательное число у: '))


def new_func(x, y):
    return x ** y


print('Результат возведения х в степень у:', new_func(x, y))

# с помощью цикла while

x = float(input('Введите действительное положительное число х: '))
y = int(input('Введите целое отрицательное число у: '))


def new_func_2(x, y):
    i = 1
    result = 1/x
    while i < abs(y):
        result = result * 1/x
        i += 1
    return result


print('Результат возведения х в степень у: ', new_func_2(x, y))
