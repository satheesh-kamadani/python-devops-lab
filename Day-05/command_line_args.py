import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print("add: ", output)
elif operation == "sub":
    output = sub(num1, num2)
    print("sub: ", output)
elif operation == "mul":
    output = mul(num1, num2)
    print("mul: ", output)
elif operation == "div":
    output = div(num1, num2)
    print("div: ", output)
else:
    print("Unknown operation:", operation)