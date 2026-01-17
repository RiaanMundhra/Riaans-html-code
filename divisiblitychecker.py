num = int(input("Enter numerator"))
den = int(input("Enter denominator"))
if num % den != 0:
    print("it isn't divisible!!")
elif num % den == 0:
    print("it is divisible!!")
else:
    print("Invalid please try again...")