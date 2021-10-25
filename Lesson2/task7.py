def equal (n):
    counter = 0
    temp = 0
    while counter < n + 1:
        temp = temp + counter
        counter += 1
    return temp, n*(n+1)//2

print(equal(50))