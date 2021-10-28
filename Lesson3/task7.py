import numpy as np
random_array = list(np.random.randint(1,10,10))
print(random_array)
random_array.sort()
print(f"Most mimimal values are {random_array[0:2]}")
