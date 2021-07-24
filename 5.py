class Stationery:
    title: str

    def draw(self):
        return print('Запуск отрисовки!')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        return print('Выполняем набросок ручкой!')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        return print('Рисуем карандашом!')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        return print('Маркер в руки и вперед!')


pen = Pen()
print(pen.title)
print(pen.draw())

pencil = Pencil()
print(pencil.title)
print(pencil.draw())

handle = Handle()
print(handle.title)
print(handle.draw())
