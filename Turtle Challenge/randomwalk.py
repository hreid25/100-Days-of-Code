from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")
tim.pensize(15)

def random_color():
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color

def new_direction(distance):
    random.choice((tim.forward,tim.backward))(distance)

def turn():
    angle = random.choice((0,90,180,270))
    return angle

def move_turtle():
    movement = True
    tim.speed(5)
    while movement == True:
        tim.pencolor(random_color())
        new_direction(50)
        tim.setheading(turn())
        
screen = Screen()
screen.colormode(255)


move_turtle()


screen.exitonclick()

