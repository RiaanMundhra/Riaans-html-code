# empty dictionary
empty = {}
print(empty)

# dictionary with values
full = {1:'one',2:'two',3:'three'}
print(full)

# accessing values in a dictionary we are using full
print(full.get(1))

# adding values to a dictionary
full[0] = 'zero'
print(full)

# updating values in a dictionary
full[1] = '1 x 1'
print(full)

#removing values from a dictionary
full.pop(3)
print(full)

#remove all values from a dictionary
full.clear()
print(full)