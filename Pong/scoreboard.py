from turtle import Turtle


class player_one(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-500,360)
        self.pensize(15)
        self.write(f"{self.score}",font=('Der Frauenhexer',75,'normal'))


class player_two(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(500,360)
        self.pensize(15)
        self.write(f"{self.score}",font=('Der Frauenhexer',75,'normal'))