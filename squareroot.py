num = int(input("Enter a number: "))
if num < 0:
    print("Cannot compute square root of a negative number.")
else:
    sqrt = num ** 0.5
    print(f"The square root of {num} is {sqrt}")
    