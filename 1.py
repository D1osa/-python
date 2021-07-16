from sys import argv
salary_script, production_param, rate_param, bonus_param = argv

production_param = float(production_param)
rate_param = float(rate_param)
bonus_param = float(bonus_param)

print("Рассчет з/п: ", salary_script)
print("Выработка в часах: ", production_param)
print("Ставка в час: ", rate_param)
print("Премия: ", bonus_param)


def script_func(argv):

    return (production_param * rate_param) + bonus_param


print('Итоговая з/п: ', script_func(argv))
