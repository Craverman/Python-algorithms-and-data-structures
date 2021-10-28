import numpy as np
random_array = list(np.random.randint(1,101,10))
print(f'Deafult array {random_array}')
min = random_array.index(min(random_array))
max = random_array.index(max(random_array))
random_array[min], random_array[max] = random_array[max], random_array[min]
print(f'New array with swapped min and max integers {random_array}')

