try:
    n = int(input("Enter a random number:"))    
    print("the square of ur number is- ", n*n)
except ValueError:
    print("invaild pls write a number")