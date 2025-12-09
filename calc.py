x = int(input("enter first number: "))
y = int(input("enter second number: "))
def add(x,y):
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}")

def subtract(x,y):
    difference = x - y
    print(f"The difference when {y} is subtracted from {x} is {difference}")

def multiply(x,y):
    product = x * y
    print(f"The product of {x} and {y} is {product}")

def divide(x,y):
    if y != 0:
        quotient = x / y
        print(f"The quotient when {x} is divided by {y} is {quotient}")
    else:
        print("Error: Division by zero is not allowed.")

disision = input("Enter the operation you want to perform (add(1), subtract(2), multiply(3), divide(4)): ")
if disision == '1':
    add(x,y)

elif disision == '2':
    subtract(x,y)

elif disision == '3':
    multiply(x,y)

elif disision == '4':
    divide(x,y)