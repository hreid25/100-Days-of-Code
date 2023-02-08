from turtle import Turtle

MOVE_DISTANCE = 60
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        current_y = self.ycor()
        self.goto(self.xcor(),current_y+MOVE_DISTANCE)

    def down(self):
        current_y = self.ycor()
        self.goto(self.xcor(),current_y-MOVE_DISTANCE)