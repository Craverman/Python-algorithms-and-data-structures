sum = 0
x = 1
n = int(input('Please insert how many times you want to divide '))
for i in range(1,n+1):
    x /= -2
    print(x)
    sum = sum + x
print(f'Your value is {sum}')