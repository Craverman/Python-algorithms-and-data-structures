integers = [232, 352, 555555, 2, 32, 231]
max = 0
number = 0
digit = 0

for el in integers:
    sum = 0
    number = el
    while (number != 0):
        sum = sum + number % 10
        number = number // 10
    if sum > max:
        max = sum
        digit = el

print(f'Your maximum integer is {digit} and sum of digits is {max}')




