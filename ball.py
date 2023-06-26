from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "circle") -> None:
        super().__init__(shape)
        self.color("white")
        self.penup()
        self.ymove = 0.3
        self.xmove = 0.3
        self.move_speed = 0.1
    def move(self):
        new_y = self.ycor() + self.ymove
        new_x = self.xcor() + self.xmove
        self.goto(new_x, new_y)
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bouncex()
    
    def bouncey(self):
        self.ymove += -1
    def bouncex(self):
        self.xmove += -1
        self.move_speed *= 0.9