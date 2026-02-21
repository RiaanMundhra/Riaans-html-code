try:
    x = int(input("write random number: "))
    n = int(input("write number to div x: "))
    print(x / n)
except ZeroDivisionError:
    print("----invaild----")
    print(" pls try again 1011")