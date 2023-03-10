import os
import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)

canvasheight = 10
canvaswidth = 10
screen.screensize(canvasheight,canvaswidth)

color_list = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]

def return_rgb():
    color = random.choice(color_list)
    return color 

def set_starting_pos():
    pass

def move_y_coordinates(current_y):
    current_y += 50
    y_coord = (0.00,current_y)
    return y_coord

tim.hideturtle()
print(screen.window_width(),screen.window_height())
dot_drawn = 0
tim.speed("fastest")
for i in range(100):
    if dot_drawn == 10:
        tim.penup()
        tim.setpos(move_y_coordinates(tim.pos()[1]))
        dot_drawn = 0
    tim.dot(20)
    dot_drawn += 1
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