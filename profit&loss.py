CP = float(input("Your CP = "))
SP = float(input("Your SP = "))
if (SP > CP):
    P = SP - CP 
    Total = (P / CP) * 100
    print("You got a profit of ",SP - CP)
    print("You got a profit percentage of",Total )
elif (SP < CP):
    L = CP - SP 
    Total = (L / CP) * 100
    print("You got a loss of ",CP - SP)
    print("You got a loss percentage of ",Total)
else:
    print("You got no profit or loss")
    print("You 0% profit/loss")