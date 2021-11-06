array = [2, -1, 3,4, -5,-7,-15,-4,-20,30,-2, 10]
max_min = -float("inf") #infinite negative value
element = 0

for el in range(0, len(array)):
    if array[el] > max_min and array[el] < 0:
        max_min = array[el]
        element = el

print(f'Your max negative value is {max_min} with index {element}')