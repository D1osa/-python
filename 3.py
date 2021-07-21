# текстовый файл выглядит так:
# Петров 30047.49
# Сидорова 40305.65
# Иванов 15576.24
# Попов 15549.13
# Умнов 50236.92
my_file = open('text_file_for_task_3', 'r', encoding='UTF-8')
low_salary = []
sal = []
for i in my_file:
        i = i.split()
        if float(i[1]) < 20000:
           low_salary.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {low_salary}, средний оклад {sum(map(float, sal)) / len(sal)}')

my_file.close()
