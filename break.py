wrd = input("Enter random word: ")

for i in range(len(wrd)):
    let = wrd[i]
    if let == 'A' or let == 'a':
        print("Found A at index", i + 1)
        break