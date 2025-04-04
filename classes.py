class Parrot:
    species = "bird"
    # consturctor
    def __init__(self,name,age):
        self.name = name
        self.age = age

wewe = Parrot("wewe",10)
hitl = Parrot("hitl",8)

print("wewe is a {}".format(wewe.age))
print("hitl is a {}".format(hitl.age))



