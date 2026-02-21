try:
    x = int(input("enter age: "))
    if x<18:
        raise ValueError
    else:
        print("valid age")
except ValueError:
    print("invalid age")
