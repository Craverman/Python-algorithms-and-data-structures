symbols = ''
counter = 0
for i in range(32, 128):
    symbols = symbols + str(i) + ' ' + chr(i) + ' '
    counter += 1
    if counter % 10 == 0:
        symbols = symbols + '\n'
print(symbols)