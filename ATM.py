wanted = int(input("Enter the amount you want to withdraw: "))
denominations = [500,100, 50, 20, 10, 5, 1]
withdrawn = {}
for denom in denominations:
    count = wanted // denom
    if count > 0:
        withdrawn[denom] = count
        wanted -= denom * count
print("You will receive:")
for denom in denominations:
    if denom in withdrawn:
        print(f"{withdrawn[denom]} x ₹{denom} notes")
