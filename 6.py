text = input('Введите слово латиницей в нижнем регистре: ')


def int_func(text):
    return text.title()


print(int_func(text))

# не уверена насчет такого решения, но вроде бы работает

new_text = input('Введите слова латиницей в нижнем регистре, разделененные пробелом: ')


def int_func(new_text):
    return new_text.title()


print(int_func(new_text))


