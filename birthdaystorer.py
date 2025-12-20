choice = int(input("Enter 1 to list a new birthday 2 to view listed birthdays: "))
if choice == 1:
    name = input("Enter the name: ")
    birthday = input("Enter the birthday (DD/MM/YYYY): ")
    with open("birthdays.txt", "a") as file:
        file.write(f"{name}: {birthday}\n")
    print("Birthday added successfully.")
elif choice == 2:
    print("Listed Birthdays:")
    with open("birthdays.txt", "r") as file:
        for line in file:
            print(line.strip())
else:
    print("Invalid choice.")