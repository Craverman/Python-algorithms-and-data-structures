import sys
print('Good Day to you, sir. Wellcome to calculator for GB. If you tyred of calculation, just press "0" as operator')
while True:
    num1 = float(input("First Number: "))
    operator = input("Operator (+, -, *, /): ")
    num2 = float(input("Second Number: "))
    out = None
    if operator == '0':
        print('Goodbye')
        sys.exit(0)
    elif operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == '/':
        try:
            out = num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by 0")
    print("Answer: " + str(out))