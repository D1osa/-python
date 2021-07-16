# нечитаемое число получается
from functools import reduce
my_gen_list = [element for element in range(100, 1000) if element % 2 == 0]
print('Список четных чисел от 100 до 1000: ', my_gen_list)

print('Произедение списка четных чисел от 100 до 1000: ', reduce(lambda x, y: x*y, my_gen_list))
