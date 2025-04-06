import turtle

class Square:

    def __init__(self,side):
        self.side = side
        self.t = turtle.Turtle()

    def draw(self):
        for _ in range(4):
            self.t.forward(self.side)
            self.t.right(90)
            
square = Square(100)
square.draw()
