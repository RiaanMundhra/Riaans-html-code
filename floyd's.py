lines = int(input("How many lines do you want to see?? "))
donelines = 0
num = 0
for i in range(lines):
    donelines = donelines + 1
    num = num + 1
    print(f"{num}" * donelines)
    