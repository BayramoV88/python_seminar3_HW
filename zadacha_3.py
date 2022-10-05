#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

import random
lst = []
for i in range(4):
    lst.append(round(random.uniform(0, 10), 2))
print(f'{lst} изначальный список')

min = 1
max = 0

for i in range(len(lst)):
    num = lst[i] % 1
    if num != 0:
        if num > max:
            max = num
        elif num < min:
            min = num
print(f'{round((max-min), 2)} - разница между дробными max и min значением дробной части')