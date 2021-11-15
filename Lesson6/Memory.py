import sys
from random import randint

#Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

symbols = ''
counter = 0
for i in range(32, 128):
    symbols = symbols + str(i) + ' ' + chr(i) + ' '
    counter += 1
    if counter % 10 == 0:
        symbols = symbols + '\n'
print(sys.getsizeof(symbols))

#Объём памяти составил 566
#Если списком выводить с первого символа (range(1, 128)), а не как сказано в задаче, то объём памяти увеличится до 715

symbols2 = symbols * 2
print(sys.getsizeof(symbols2))

#Создав новую переменную, умножив на два изначальную, объём занимаемой памяти аналогино возрос практически в 2 раза: 1083

"""//////////////////////////////////////////////////////////////////////"""

#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import numpy as np
random_array = list(np.random.randint(1,101,100))
min = random_array.index(min(random_array))
max = random_array.index(max(random_array))
random_array[min], random_array[max] = random_array[max], random_array[min]
print(sys.getsizeof(random_array))

#Объём памяти составил 136
#Если значения величину значений увеличить до 100 (1, 101, 100), то задействованная память увеличится до 856.

"""//////////////////////////////////////////////////////////////////////"""

#Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

size = 5
sum = 0
matrix = [[randint(1,100) for el in range(size)] for el in range(size)]
for el in range(0,len(matrix)):
    sum = np.array(matrix[el]).sum()
    matrix[el].append(sum)
print(sys.getsizeof(matrix))

# Матрица размером 4х4 занимает 88 бит, увеличив на единицу, то объём памяти увеличится до 120.

