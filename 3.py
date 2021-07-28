class Cell:

    def __init__(self, cells_number):
        self.cells_number = int(cells_number)

    def __str__(self):
        return f'Результат операции {self.cells_number * "*"}'

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        return self.cells_number - other.cells_number if (self.cells_number - other.cells_number) > 0 else print(
            'Отрицательный результат')

    def __mul__(self, other):
        return Cell(int(self.cells_number * other.cells_number))

    def __truediv__(self, other):
        return Cell(round(self.cells_number // other.cells_number))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cells_number / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.cells_number % cells_in_row)}'
        return row


c_1 = Cell(5)
c_2 = Cell(12)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_2 / c_1)
print(c_1.make_order(2))
print(c_2.make_order(6))
