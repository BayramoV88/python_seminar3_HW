#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
fibonacci = []
a, b = 1, 1
for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b
a, b = 0, 1
for i in range (n+1):
    fibonacci.insert(0, a)
    a, b = b, a - b
print(f'{fibonacci} - список чисел Фибоначчи')