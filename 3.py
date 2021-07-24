class Worker:
    name: str
    surname: str
    position: str
    _income = dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}, должность: {self.position}'

    def get_total_income(self):
        total_income = sum(self._income.values())
        return f'Общий доход: {total_income} руб'


worker_1 = Position('Анатолий', 'Петров', 'директор', 100000, 30000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())

worker_2 = Position('Иван', 'Борисов', 'заместитель директора', 90000, 25000)
print(worker_2.get_full_name())
print(worker_2.get_total_income())

worker_3 = Position('Аркадий', 'Степанов', 'секретарь', 70000, 20000)
print(worker_3.get_full_name())
print(worker_3.get_total_income())
