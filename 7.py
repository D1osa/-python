# вот такой начальный текстовый файл
# firm_1 OOO 500000 50000.
# firm_2 OAO 250000 30000.
# firm_3 OAO 300000 40000.
import json
import os
DIR = 'files'
file_to_read_path = os.path.join(DIR, 'task_7')
file_to_write_path = os.path.join(DIR, 'task_7.json')

result = []
profit = {}
average = []

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    counter = 1
    while True:
        line = file_read.readline().split()

        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1


result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_to_write_path, 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write)

# вот такой в итоге json
# [{"firm_1": 450000.0, "firm_2": 220000.0, "firm_3": 260000.0}, {"average_profit": 310000.0}]
