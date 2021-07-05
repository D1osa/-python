a = int(input('Сколько км в первый день: '))
b = int(input('Сколько км достичь: '))
i = 1
while a < b:
    a *= 1.1
    i += 1
print(f'На {i} день')