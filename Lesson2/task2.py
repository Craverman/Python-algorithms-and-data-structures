numbers = list(input("Insert some digits: "))
numbers = map(int, numbers)
chet = 0
nechet = 0
for i in numbers:
    if i % 2 == 0:
        chet += 1
    else:
        nechet +=1
print(f'Chet is {chet} and nechet is {nechet}' )