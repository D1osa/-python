name = input('Как Вас зовут? ')
surname = input('Введите Вашу фамилию: ')
age = input('Введите год рождения: ')
city = input('Ваш город: ')
email = input('Введите email: ')
mobile = input('Введите номер телефона: ')


def users_data(*args):
    return args


print(users_data(name, surname, age, city, email, mobile))
