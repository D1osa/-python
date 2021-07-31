class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


number_1 = float(input('Введите делимое: '))
number_2 = float(input('Введите делитель: '))
try:
    if number_2 == 0:
        raise OwnException('На ноль делить нельзя!')
    res = number_1 / number_2
except OwnException as error:
    print(error)
else:
    print(f'Данные введены верно, частное: {res:.2f}')
