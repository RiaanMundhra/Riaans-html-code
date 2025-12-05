absent = int(input("Enter number of absent days: "))
if absent >= 5 * 365 / 100:
    print("You are not allowed to sit for the exam due to high absenteeism.")
else:
    print("You are allowed to sit for the exam.")