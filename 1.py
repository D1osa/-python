class Date:
    def __init__(self, day_mon_year):
        self.day_mon_year = str(day_mon_year)

    @staticmethod
    def my_date(day, month, year):
        if 1 <= day <= 31:
            print('ok day')
        else:
            print('Нет такого дня!')
        if 1 <= month <= 12:
            print('ok month')
        else:
            print('Неверный месяц!')
        if 2021 >= year >= 0:
            print('ok year')
        else:
            print('Этот год еще не наступил!')

    @classmethod
    def date(cls, day_mon_year):
        date = []
        for i in day_mon_year.split():
            if i != '-':
                date.append(i)
        return f'{int(date[0])}.{int(date[1])}.{int(date[2])}'

    def __str__(self):
        return f'Текущая дата {Date.date(self.day_mon_year)}'


d = Date('28 - 7 - 2021')
print(d)
print(Date.my_date(12, 13, 2019))
print(Date.my_date(1, 9, 2023))
print(Date.my_date(24, 9, 1991))
print(Date.my_date(37, 24, 2069))
print(Date.date('24 - 11 - 2001'))
print(d.date('11 - 12 - 2005'))
print(d.my_date(23, 7, 2020))
