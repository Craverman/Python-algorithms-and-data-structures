a = int(input('First side '))
b = int(input('Second side '))
c = int(input('Third side'))
if a + b > c and a + c > b and b + c > a:
    print('Proper triangle')
    if a == b and c:
        print('Isosceles')
    elif a == b == c:
        print("Equilateral triangle")
    else:
        print("Scalene triangle")
else:
    print('Not a triangle')
