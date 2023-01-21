num1 = float(input("What is the first number:  "))
op = input("What type of operator are you using?: ")
num2 = float(input("What is the second number:  "))


def div(num1, num2):
    answer = float(num1/num2)
    return print(answer)


def mult(num1, num2):
    answer = float(num1*num2)
    return print(answer)


def add(num1, num2):
    answer = float(num1+num2)
    return print (answer)


def sub(num1, num2):
    answer = float(num1-num2)
    return print(answer)


if op == "+":
    add(num1, num2)
elif op == "-":
    sub(num1, num2)
elif op == "*":
    mult(num1, num2)
elif op == "/":
    div(num1, num2)
else:
    print("Invalid operator")

