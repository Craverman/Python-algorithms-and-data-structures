import numpy as np
random_array = list(np.random.randint(1,101,10))
random_array.sort()
sum = 0
for el in range(1, len(random_array)-1):
    sum = sum + random_array[el]
print(random_array)
print(f'Sum of your values from min to max is {sum}')