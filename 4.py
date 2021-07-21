rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
my_file = open('text_file_for_task_4', 'r')
for i in my_file:
    i = i.split(' ', 1)
    new_file.append(rus_dict[i[0]] + ' ' + i[1])
    print(new_file)
my_file.close()
new_file_2 = open('new_text_4', 'w')
new_file_2.writelines(new_file)
new_file_2.close()
