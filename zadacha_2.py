# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
lst = []
for i in range(6):
    lst.append(random.randint(0, 10))
print(f'{lst} изначальный список')

new_lst = []
for i in range(len(lst) // 2):
    new_lst.append(lst[i] * lst[-1-i])
print(f'{new_lst} новый список')