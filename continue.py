for x in range(0,2145677):
    if x % 10 == 0:
        print("twistbuzz")
        continue
    if x % 15 == 0:
        print("fizzbuzz")
        continue
    else:
        if x % 5 == 0:
            print("buzz")
            continue
        if x % 3 == 0:
            print("fizz")
        else:
            print(x)