from turtle import Turtle, Screen
import random

# Create a title screen and a "Start Game" & "End" option
# grow the snake each time it eats food
# randomize the location of the food
# If the snake hits itself or the edge of the screen, the snake dies and the game restarts

screen = Screen()
screen.setup(width=1000,height=800)
screen.bgcolor("black")
screen.title("Let's Play the Snake Game")

def create_snake_body():
    x = -30
    y = 0
    for i in range(3):
        snk = Turtle(shape="square")
        snk.color("white")
        x += 20
        snk.goto(x, y)

def place_food():
    x = random.randint(-480,480)
    y = random.randint(-380,380)
    food = Turtle(shape="circle")
    food.color("blue")
    food.penup()
    food.goto(x=x,y=y)
    # randomize the location of the food on the screen

def food_eaten():
    pass
    # listen for when the snake has touched the piece of food, return boolean

def move_snake():
    # Listen for snake movement actions
    pass

create_snake_body()
place_food()







screen.exitonclick()