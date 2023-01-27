from turtle import Turtle, Screen
import random
import time

# Create a title screen and a "Start Game" & "End" option
# grow the snake each time it eats food
# randomize the location of the food
# If the snake hits itself or the edge of the screen, the snake dies and the game restarts

screen = Screen()
screen.setup(width=1000,height=800)
screen.bgcolor("black")
screen.title("Let's Play the Snake Game")
# tracer disables when value 0 is passed through
screen.tracer(0)
screen.listen()

def up():
    screen.turtles()[2].setheading(180)

def down():
    screen.turtles()[2].setheading(270)

def right():
    screen.turtles()[2].setheading(0)

def left():
    screen.turtles()[2].setheading(90)

def create_snake_body(number):
    x = -30
    y = 0
    for i in range(number):
        snk = Turtle(shape="square")
        snk.color("white")
        snk.penup()
        x += 20
        snk.goto(x, y)
    return snk

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

def update_positions(snake_index):
    new_x = screen.turtles()[snake_index - 1].xcor()
    new_y = screen.turtles()[snake_index - 1].ycor()
    screen.turtles()[snake_index].goto(new_x,new_y)


create_snake_body(3)
screen.update()
# place_food()



snk_body = [i for i in screen.turtles()]

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for snk_index in range(len(snk_body) - 1, 0, -1):
        update_positions(snk_index)
    snk_body[0].forward(20)
    # snk_body[0].left(90)
    screen.onkey(key="A".lower(), fun=up)
    screen.onkey(key="D".lower(), fun=right)
    screen.onkey(key="S".lower(), fun=down)
    screen.onkey(key="W".lower(), fun=left)


screen.exitonclick()
