# итератор, повторяющий элементы некоторого списка, определенного заранее
from itertools import cycle
my_cycle = ('один', 23, True, 11)
i = 0
for el in cycle(my_cycle):
    if i > 10:
        break
    print(el)
    i += 1
