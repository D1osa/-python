revenue = int(input('Введите значение вышей выручки: '))
costs = int(input('Введите значение ваших издержек: '))
if revenue > costs:
    profit = revenue - costs
    rent = profit / revenue
    print('Вы получаете прибыль! Рентабельность равна', rent)
    employee = int(input('Введите количество сотрудников вашей фирмы: '))
    print('Прибыль фирмы в рассчете на одного сотрудника', profit // employee)
else:
    print('Вы работаете в убыток!')
