x = int(input("Введите необходимое число "))
suma = 0
mult = 1

while x > 0:
    digit = x % 10
    suma = suma + digit
    mult = mult * digit
    x = x // 10

print("Сумма вашего числа =", suma)
print("Произведение вашего числа =", mult)