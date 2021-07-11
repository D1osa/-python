rating_list = [7, 5, 3, 3, 2]
users_var = int(input('Введите число: '))
rating_list.append(users_var)
rating_list.sort(reverse=True)
print(rating_list)
