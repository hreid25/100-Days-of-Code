import sqlite3
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial',20,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def game_ended(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        # DB should be updated with the users score here
    def user_scored(self):
        # increase score
        self.score += 100
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)



