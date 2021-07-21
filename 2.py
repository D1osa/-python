my_file = open('text_file_for_task_2', 'r')
my_lines = my_file.readlines()
print(f'В файле {len(my_lines)} строк(и)')
i = 1
for word in my_lines:
    print(f'В {i} строке {len(word.split())} слов(а)')
    i += 1
my_file.close()
