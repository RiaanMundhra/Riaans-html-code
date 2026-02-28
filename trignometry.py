import math
choice = int(input("what do you want sin = 1 / cos = 2 / tan = 3 "))
angle = int(input("what is the angle "))
h = int(input("what is the hypotenus"))

if choice == 1:
    o = sine(angle) * h
    print(o)
if choice == 2:
    a = cosine(angle) * h
    print(a)
if choice == 3:
    o = tangent(angle) * a
    print(o)
   # SOHCAHTOA