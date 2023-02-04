from turtle import Turtle, Screen
from divider import Divider
from ball import Ball
from scoreboard import player_one,player_two

screen = Screen()
screen.bgcolor("black")
screen.screensize(1000,1000)
screen.tracer(0)

ball = Ball()
divide_screen = Divider()
p1_score = player_one()
p2_score = player_two()

game_on = True
while game_on:
    screen.update()
    pass




screen.exitonclick()