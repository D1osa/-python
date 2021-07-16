from random import randint
gen_list = [randint(1, 100) for i in range(10)]
print(gen_list)
new_gen_list = []

for i in range(len(gen_list)-1):
    if gen_list[i+1] > gen_list[i]:
        new_gen_list.append(gen_list[i+1])
print(new_gen_list)
