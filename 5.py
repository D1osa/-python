class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        return f'Сумма комплексных чисел равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел равно: {self.a * other.a} + {self.b * other.b} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


complex_1 = ComplexNumber(2, 3)
complex_2 = ComplexNumber(4, 5)
print(f'Комплексное число 1: {complex_1}, комплексное число 2: {complex_2}')
print(complex_1 + complex_2)
print(complex_1 * complex_2)
