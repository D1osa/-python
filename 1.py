# перебрала кучу вариантов, но записывается в файл все равно в одну строку без пробела
# не понимаю, что с этим делать
my_new_file = open('my_new_file', 'w', encoding='utf-8')
my_new_file.write(input('Введите имя: \n'))
my_new_file.write(input('Введите фамилию: \n'))
my_new_file.write(input('Введите возраст: \n'))
my_new_file.close()
my_new_file = open('my_new_file', 'r', encoding='utf-8')
for line in my_new_file:
    print(line)
my_new_file.close()
