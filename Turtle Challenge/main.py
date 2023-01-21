from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
start_position = tim.position()

def random_color():
    color = (randint(1,255),randint(1,255),randint(1,255))
    return color

screen = Screen()
screen.colormode(255)

sides = [{'triangle':3, 'square':4, 'pentagon':5, 'hexagon':6, 'heptagon':7, 'octagon':8, 'nonagon':9, 'decagon':10}]
angles = {k:360/v for k,v in sides[0].items()}

for shape, angle in angles.items():
    print("shape: ", shape, "| angle: ", angle)
    tim.pencolor(random_color())
    for turn in range(sides[0][shape]):
        tim.forward(100)
        tim.right(angle)

screen.exitonclick()

# Each time it progresses by the same distance, it chooses a new direction and changes color
# random walk. Increase line thickness and speed up the turtle.



