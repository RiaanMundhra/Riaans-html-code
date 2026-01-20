consumed = int(input("enter the amount of voltage you have consumed"))
bill = consumed * 2
num = int(input(f"Your bill is {bill} what is your payment method 1 - for cash 2 - for card"))
if num == 1:
    cash = int(input(f"Pls give {bill} amount in cash"))
    if cash != bill:
        print("Wrong amount --- invaild")
    else:
        print("thank you for your time")
elif num == 2:
    card = str(input("Pls give your card no"))
    if len(str(card)) == 8:
        pin = str(input("now give your pin please"))
        if len(str(pin)) == 4:
           print("thank you for your time")
           
        else:
            print("invalid pin")    
    else:
        print("invalid card")
rating = str(input("how did you like the software??"))
if rating == 5:
    print("thank you")
    
elif rating < 5:
    feedback = str(input("what could we do better??"))