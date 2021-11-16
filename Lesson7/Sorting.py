#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import numpy as np
import random

def bubble_sort(some_list):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(some_list) - 1):
            if some_list[i] > some_list[i+1]:
                some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
                swapped = True

random_array = list(np.random.randint(-100,101,10))
print(f'Unsorted list {random_array}')
bubble_sort(random_array)
print(f'Sorted list using bubble sort {random_array}')

#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

random_array2 = list(np.random.randint(-100,101,10))
print(f'Unsorted list {random_array2}')
mergeSort(random_array2)
print(f'Sorted list using merge sort {random_array2}')

#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
#которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
#Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

def median(l, half):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    pivot = l[0]
    less = []
    more = []
    pivots = []

    for item in l:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))

n = 6
array = [random.randint(-100, 100) for el in range(2 * n + 1)]
print(f'Original array {array}')
print(f'Median {median(array, n)}')