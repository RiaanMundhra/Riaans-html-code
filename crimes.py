try:
    age = int(input("enter age... "))
    essential = 0
    
    if age < essential:
        raise ValueError
    else:
        print("valid age...")
        
except ValueError:
    print("This is an incorrect age pls check the details...")