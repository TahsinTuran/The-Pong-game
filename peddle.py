from turtle import Turtle

class Peddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        self.color("white")

    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
