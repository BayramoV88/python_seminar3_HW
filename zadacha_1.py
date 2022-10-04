# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
lst = []
for i in range(7):
    lst.append(random.randint(0, 30))
print(f'{lst} изначальный список')

sum = 0
for i in range(0, len(lst)):
    if i % 2 != 0:
        sum = sum + lst[i]
print(f'Сумма элементов на нечетных позициях = {sum}')