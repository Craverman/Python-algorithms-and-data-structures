import numpy as np
array1 = np.random.randint(1,101,10)
array2 = []

for el in range(0,len(array1)):
    if array1[el]%2 ==0:
        array2.append(el)
print(array1)
print(array2)

