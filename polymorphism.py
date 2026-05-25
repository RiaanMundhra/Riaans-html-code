class square():
    def __init__(self, side):
        self.side = side
    def area(self):
        s = self.side * self.side
        print(s)
class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        c = self.radius * self.radius * 22/7
        print(c)
objsq = square(14)
objcir = circle(7)

for i in (objsq, objcir):
    i.area()