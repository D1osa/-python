class MyException(Exception):
    def __init__(self, text):
        self.text = text


result_list = []
while True:
    i = input('Введите число или stop для прекращения: ')
    if i == 'stop':
        print(f'Получился такой список {result_list}')
        break
    try:
        if not i.isnumeric():
            raise MyException('Вы ввели не число!')
        result_list.append(int(i))
    except MyException as error:
        print(error)
