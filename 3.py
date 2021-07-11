# словарь

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# список
# перерыла много интернета, как по-другому это сделать красиво в 'одну строчку' - не понимаю
# зато сама =)

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
for i in list(winter):
    if month == i:
        print('Winter')
for i in list(spring):
    if month == i:
        print('Spring')
for i in list(summer):
    if month == i:
        print('Summer')
for i in list(autumn):
    if month == i:
        print('Autumn')
