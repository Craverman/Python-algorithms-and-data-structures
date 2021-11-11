from numpy import random
x = random.randint(0, 100)
z = 1
while z <= 10:
    guessing = int(input('Try to guess a number: '))
    z += 1
    if guessing > x:
        print("Too large, try again")
    elif guessing < x:
        print("Too small, try again")
    elif guessing == x:
        print("Congratulations, you are winner!")
        break
print(f'Right answer is {x}')
