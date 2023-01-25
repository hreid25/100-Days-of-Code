from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
     tim.left(10)

def move_clockwise():
     tim.right(10)

def clear_screen_reset():
     screen.resetscreen()
     
screen.listen()

# screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="A".lower(), fun=move_counterclockwise)
screen.onkey(key="D".lower(), fun=move_clockwise)
screen.onkey(key="S".lower(), fun=move_backwards)
screen.onkey(key="W".lower(), fun=move_forwards)

screen.onkey(key="C", fun=clear_screen_reset)

screen.exitonclick()

#  Passing functions to a function will be useful when listening for events.