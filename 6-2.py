product_dict = []
i = 1
while True:
    product_dict.append(
        (input('Введите номер товара: '), dict({
            'name': input('Введите название товара: '),
            'price': float(input(' Введите стоимость товара: ')),
            'units': input('Введите единицы измерения товара: ')
        }))
    )
    if(input('Данные добавлены. Ввести новый товар? да/нет ')) == 'нет':
        break
    i += 1
print('Список товаров:', product_dict)

# result_dict = dict({})
# for product in product_dict:
    # for key, val in product.items():
        # if key in result_dict:
            # result_dict[key].extend(val)
    # else:
        # result_dict[key] = val
# print('Результат обработки данных', result_dict)

# тут я не понимаю, как работать со словарем

# в методичке такого нет, а в интернете написано не понятно и ничего не работает
