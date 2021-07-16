from random import randint
list_of_numbers = [randint(1, 10) for i in range(20)]
print('Исходный сгенерированный список чисел: ', list_of_numbers)
unique_list = []
for i in list_of_numbers:
    if i in unique_list:
        continue
    else:
        unique_list.append(i)

print('Уникальный список чисел: ', unique_list)
