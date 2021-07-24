class Road:
    _lenght = int
    _width = int

    def __init__(self, lenght: int, width: int):
        self._lenght = lenght
        self._width = width

    def calculate(self, weight: int, depth: int):
        return int(self._lenght * self._width * weight * depth / 1000)


lenght, width, weight, depth = [int(x) for x in (
    input('Введите длину, ширину, массу асфальта, толщину покрытия через пробел: ').split())]
r = Road(lenght, width)
print(f'Необходимая масса асфальта {r.calculate(weight, depth)} тонн')
