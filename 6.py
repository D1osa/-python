# текстовый файл выглядит так:
# Химия: 12(л)  30(п)  15(лаб)
# Биология: 10(л)  -  8(лаб)
# Физкультура: -  30(п)  -
import os
import re

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'task_6')


def calculate_hours(calc_line: str):
    line_of_hours = re.sub(r'\D', ' ', calc_line)
    total_hours = 0
    for hour in line_of_hours.split():
        total_hours += float(hour)
    return total_hours


overall_subject_info = {}
with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    for line in file_read.readlines():
        listed_line = line.split(': ')
        overall_subject_info[listed_line[0]] = calculate_hours(listed_line[1])

print(f'Всего часов по предметам:\n {overall_subject_info}')
