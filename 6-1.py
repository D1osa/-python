# итератор, генерирующий целые числа, начиная с указанного
from itertools import count
for el in count(int(input('Введите число меньше 25: '))):
    if el > 25:
        break
    else:
        print(el)
