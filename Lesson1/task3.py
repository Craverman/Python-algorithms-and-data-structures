import matplotlib.pyplot as plt
import numpy as np
x1 = int(input('Please, insert x1: '))
x2 = int(input('Please, insert x2: '))
y1 = int(input('Please, insert y1: '))
y2 = int(input('Please, insert y2: '))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print('slope: ', k)
print('intercept: ', b)
x = np.linspace(-5,5,100)
y = k*x+b
plt.plot(x, y, '-r', label=f'y={k}x+{b}')
plt.title(f'Graph of y={k}x+{b}')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
