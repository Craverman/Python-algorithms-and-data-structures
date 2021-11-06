from random import randint
size = 5
matrix = [[randint(1,100) for el in range(size)] for el in range(size)]
for el in matrix:
    print(el)

minColumn = list(map(min, zip(*matrix)))

print(f'Miminal values of each columns are {minColumn} and max value of them is {sorted(minColumn)[-1]}' )


