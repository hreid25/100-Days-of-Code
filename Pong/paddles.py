from turtle import Turtle

MOVE_DISTANCE = 60
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1,stretch_len=5)
        self.goto(position)

    def up(self):
        self.setheading(UP)
        current_y = self.ycor()
        self.goto(self.xcor(),current_y+MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        current_y = self.ycor()
        self.goto(self.xcor(),current_y-MOVE_DISTANCE)