numbers = list(input("Insert your numbers: "))
numbers = map(int, numbers)
digit = int(input("Insert digit: "))
counter = 0
for el in numbers:
    if el == digit:
        counter +=1
if counter > 1:
    print(f'Your digit {digit} is repeating {counter} times')
else: print(f'Your digit {digit} is repeating {counter} time')



