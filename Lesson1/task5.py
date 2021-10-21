a = input('First letter: ')
b = input('Second letter: ')
alplhabet = list(map(chr, range(ord('a'), ord('z')+1)))
for i in range(0, len(alplhabet)):
    if alplhabet[i] == a:
        a = i+1
    elif alplhabet[i] == b:
        b = i+1
if a > b:
    c = a - b
else:
    c = b - a
print(f'first letter is {a}, second letter is {b}, between first and second {c-1} letters')
