import cProfile

def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1

def non_eratosthenes(n):
    s = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)] for i in sub]]
    return s #с использованием list comprehension для всей функции
    # время на исполнение стандартного подсчёта резко увеличивается в разы,поэтому значение было взято меньше

def eratosthenes_stat():
   n = 10000000
   eratosthenes(n)
def non_eratosthenes_stat():
    n = 8000
    non_eratosthenes(n)

cProfile.run('eratosthenes_stat()')
cProfile.run('non_eratosthenes_stat()')
"""
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.331    0.331 <string>:1(<module>)
        1    0.030    0.030    0.030    0.030 task2.py:11(<listcomp>)
        1    0.008    0.008    0.331    0.331 task2.py:18(eratosthenes_stat)
        1    0.284    0.284    0.322    0.322 task2.py:4(eratosthenes)
        1    0.000    0.000    0.331    0.331 {built-in method builtins.exec}
    78498    0.008    0.000    0.008    0.000 {built-in method builtins.len} 
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.050 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   46.341   46.341 <string>:1(<module>)
        1    0.000    0.000   46.341   46.341 task2.py:14(non_eratosthenes)
        1    5.199    5.199   46.341   46.341 task2.py:15(<listcomp>)
        1    0.000    0.000   46.341   46.341 task2.py:21(non_eratosthenes_stat)
        1    0.000    0.000   46.341   46.341 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""