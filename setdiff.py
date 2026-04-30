def getsets(prompt):
    user_input = input(prompt)
    return set(map(int, user_input.split()))

set1 = getsets("Enter numbers for Set 1: ")
set2 = getsets("Enter numbers for Set 2: ")

result = set1.symmetric_difference(set2)

print("Symmetric Difference:", result)