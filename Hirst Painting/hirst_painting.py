import os
import colorgram
from turtle import Turtle, Screen
import random

# reset the turtles position once it reaches the edge of the window
# Move tim up 50 from the leftmost dot from the opposite edge and repeat the dotting process.

tim = Turtle()
tim.shape("turtle")
# tim.color("coral")
screen = Screen()
screen.colormode(255)
screen.screensize(100, 100)

color_list = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]

def return_rgb():
    color = random.choice(color_list)
    print(color)
    return color 

for i in range(100):
    if tim.pos() == (850.00,0.00):
        tim.setpos(0.00,50.00)
    print(tim.pos(), i)
    tim.dot(20)
    tim.penup()
    tim.pencolor(return_rgb())
    tim.forward(50)
    tim.pendown()

screen.exitonclick()


# colors = colorgram.extract('C://Users//haydr//100 Days of Code///Hirst Painting//damien_hirst.jpg', 10)

# rgb_list = [i.rgb for i in colors]
# color_list = []
# for i, value in enumerate(rgb_list):
#     color_list.append(tuple((rgb_list[i].r,rgb_list[i].g,rgb_list[i].b)))
# print(color_list)