from turtle import Turtle

class Divider(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(5)
        self.penup()
        self.goto(0,-480)
        self.setheading(90)
        self.hideturtle()
        self.draw_divider()
    
    def draw_divider(self):
        dashes = int(480 / 20)
        x = 20
        # print(dashes)
        for i in range(dashes):
            self.pendown()
            self.forward(x)
            self.penup()
            self.forward(x)


