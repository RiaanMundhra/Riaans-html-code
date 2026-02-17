a = int(input("Pls give a number: "))
b = int(input("Pls give a smaller number than a: "))
form = int(input("what do you want to do 1add 2sub 3 mul 4 div"))

if form == 1:
    total =  a + b
    print(total)
    pass
elif form == 2:
    total =  a - b
    print(total)
    pass
elif form == 3:
    total =  a * b
    print(total)
    pass
elif form == 4:
    total =  a / b
    print(total)
    pass
else:
    print("invalid")