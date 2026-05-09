import random
ans = int(input("Do you want us to create a random password for u?? 1 for yes 2 for no: "))
def newpass():
    password  =  random.randint(0,999999)
    print(password)
if ans == 1:
    newpass()
elif ans == 2:
    print("ok tell me when you want it...")
else:
    print("I'm sorry but I couldn't catch that...")