from random import randint
import numpy as np

size = 4
sum = 0
matrix = [[randint(1,100) for el in range(size)] for el in range(size)]
for el in range(0,len(matrix)):
    sum = np.array(matrix[el]).sum()
    matrix[el].append(sum)
    print(matrix[el])



