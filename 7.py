import math


def fact_func(n):
    for el in range(n):
        el += 1
        yield el


a = fact_func(int(input('Введите число: ')))


print(type(a))
for b in a:
    print(b)
print(f'Факториал числа равен: {math.factorial(b)}')
