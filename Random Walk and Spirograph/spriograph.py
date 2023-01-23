from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
tim.color("coral")
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color

def draw_sprio(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(60)
        tim.pencolor(random_color())
        tim.setheading(tim.heading() + size_of_gap)

draw_sprio(5)

screen.exitonclick()