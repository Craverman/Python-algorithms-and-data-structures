from numpy import random
x = int(input('Введите число а: '))
y = int(input('Введите число b: '))
a = input('Введите любой символ: ')
b = input('Введите любой символ: ')
print(f'Случайное целое число: {random.randint(x,y)}')
print(f'Случайное вещественное число: {random.uniform(x,y)}')
print(f'Случайный символ: {random.choice([chr(i) for i in range(ord(a), ord(b))])}')


