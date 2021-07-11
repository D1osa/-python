list_of_words = input('Введите несколько слов: ')
list_of_words = list_of_words.split(' ')
for ind, el in enumerate(list_of_words):
    print(f'{ind}. {el[:10]}')
