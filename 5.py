def summary():
    with open('file_5.txt', 'w+') as file_obj:
        line = '357 421 142'
        file_obj.writelines(line)
        my_numb = line.split()

        print('Сумма чисел: ', sum(map(int, my_numb)))


summary()
