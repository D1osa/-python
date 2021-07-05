seconds = int(input('введите время в секундах '))
#в часе 3600 сек
hours = seconds // 3600
second_s = seconds % 3600 #общее количество секунд разделить на кол-во секунд в часе и взять остаток
minutes = second_s // 60 #60 сек в минуте
sec = seconds % 60 #деление с остатком
print(f'{hours} : {minutes} : {sec}')


