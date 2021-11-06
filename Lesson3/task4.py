array = [0,2,3,65,2,4,7,3,2,7,8,9,2,3,2]
def most_common(lst):
    return max(set(lst), key=lst.count)
print(f'Most common value is {most_common(array)}')