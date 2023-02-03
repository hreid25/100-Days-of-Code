from turtle import Turtle, Screen
from divider import Divider
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.screensize(1000,1000)

ball = Ball()
divide_screen = Divider()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    pass




screen.exitonclick()