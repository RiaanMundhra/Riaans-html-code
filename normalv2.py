import random

def win():
    print("you have won the match!!")
def lose():
    print("better luck next time!!")
ans = str(input("Do you want to play the gambling game?? "))
if ans == "yes":
    money = int(input("how much do you want to bet?? "))
    num = random.randint(1, 2)
    if num == 1:
        win()
        money = money * 2
        print(money)
    if num == 2:
        lose()
        print("you lost:", money)
else:
    print("Broke boy")