num = int(input("Enter a number: "))
if num >= 50:
    if num%2 == 0:
        print("The number is greater than or equal to 50 and even.")
    else:
        print("The number is greater than or equal to 50 and odd.")

else:
    if num%2 == 0:
        print("The number is less than 50 and even.")
    else:
        print("The number is less than 50 and odd.")