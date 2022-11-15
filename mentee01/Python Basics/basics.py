#this is a basic calculater
#variables
x = input("first number")
operater = input ("choose a function") 
y = input("second number")

#data cleaning (turn str into int)
x = int(x)
y = int(y)


def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

# If statments

if operater == "+":
    print(sum(x, y))

if operater == "-":
    print(sub(x, y))

if operater == "*":
    print(multiply(x, y))

if operater == "/":
    print(division(x, y))
