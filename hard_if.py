print("Welcome to the square finder!!")

def square():
    num1 = int(input("Enter a number to find its square: "))
    if num1 >= 0:
        result = num1 * num1
        print(f"The square of {num1} is {result}.")
    else:
        print("Please enter a non-negative number.")

def root():
    num = int(input("Enter a number to find its square root: "))
    if num >= 0:
        result = num ** 0.5
        print(f"The square root of {num} is {result}.")
    else:
        print("Please enter a non-negative number.")

choice = input("Type 'square' to find the square or 'root' to find the square root: ").strip().lower()

if choice == 'square':
    square()
elif choice == 'root':
    root()
else:
    print("Invalid choice. Please type 'square' or 'root'.")
