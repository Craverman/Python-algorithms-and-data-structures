import cProfile
from statistics import mode
import numpy as np
#Возьмём для примера три варианта поиска наиболее часто повторяющихся чисел:
def most_common(lst):
    return max(set(lst), key=lst.count)

def most_common2(lst):
   return mode(lst)

def most_common3(lst):
   return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]


def first_var():
   array = list(np.random.randint(1,100,1000000))
   most_common(array)
   #Встроенный метод builin тратит на подсчёт: 2.136
def second_var():
   array = list(np.random.randint(1,100,1000000))
   most_common2(array)
   #Очень удобная функция модуля statistics, на удивление справляется за долю секунды.
def third_var():
   array = list(np.random.randint(1, 100, 1000000))
   most_common3(array)
   #Больше всего тратится на встроенный метод count: 2.132

cProfile.run('first_var()')
cProfile.run('second_var()')
cProfile.run('third_var()')

"""
16 function calls in 2.243 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(prod)
        1    0.011    0.011    2.243    2.243 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2928(_prod_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2933(prod)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
        1    0.047    0.047    2.232    2.232 task1.py:14(first_var)
        1    0.038    0.038    2.174    2.174 task1.py:5(most_common)
        1    0.000    0.000    2.243    2.243 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    2.136    2.136    2.136    2.136 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.010    0.010    0.010    0.010 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}


         58 function calls (40 primitive calls) in 0.176 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(prod)
        1    0.011    0.011    0.176    0.176 <string>:1(<module>)
        1    0.000    0.000    0.108    0.108 __init__.py:581(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:600(most_common)
        1    0.000    0.000    0.108    0.108 __init__.py:649(update)
       10    0.000    0.000    0.000    0.000 _collections_abc.py:409(__subclasshook__)
     10/1    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2928(_prod_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2933(prod)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
        1    0.000    0.000    0.000    0.000 heapq.py:521(nlargest)
        1    0.000    0.000    0.108    0.108 statistics.py:534(mode)
        1    0.046    0.046    0.165    0.165 task1.py:18(second_var)
        1    0.000    0.000    0.108    0.108 task1.py:8(most_common2)
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
     10/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.108    0.108    0.108    0.108 {built-in method _collections._count_elements}
        1    0.000    0.000    0.176    0.176 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.010    0.010    0.010    0.010 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}


         314 function calls in 2.241 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(prod)
        1    0.011    0.011    2.241    2.241 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2928(_prod_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2933(prod)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
        1    0.039    0.039    2.172    2.172 task1.py:11(most_common3)
      100    0.001    0.000    2.133    0.021 task1.py:12(<genexpr>)
       99    0.000    0.000    0.000    0.000 task1.py:12(<lambda>)
        1    0.047    0.047    2.230    2.230 task1.py:22(third_var)
        1    0.000    0.000    2.241    2.241 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.001    0.001    2.133    2.133 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
       99    2.132    0.022    2.132    0.022 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.010    0.010    0.010    0.010 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
"""