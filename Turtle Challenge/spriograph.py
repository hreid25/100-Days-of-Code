from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
tim.color("coral")
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
    color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    return color

def draw_sprio():
    spirograph = True
    while spirograph == True:
        tim.circle(60)
        tim.pencolor(random_color())
        tim.setpos(0.00,0.00)
        tim.right(15)

draw_sprio()

screen.exitonclick()