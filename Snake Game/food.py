from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.speed("fastest")
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        self.goto(x,y)
        self.touched_food()

    def touched_food(self):
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        self.goto(x,y)