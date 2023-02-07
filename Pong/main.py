from turtle import Turtle, Screen
from divider import Divider
from ball import Ball
from scoreboard import player_one,player_two
from paddles import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(1000,1000)
screen.title("Pong")
screen.tracer(0)
# Create ball
ball = Ball()
# Create Dividing line
divide_screen = Divider()
# Initialize player score displays
p1_score = player_one()
p2_score = player_two()
# Initialize player paddles
p1_paddle = Paddle((-775,0))
p2_paddle = Paddle((775,0))
# Listen for inputs
screen.listen()
# PADDLE ONE CONTROLS
screen.onkey(p1_paddle.up,"W".lower())
screen.onkey(p1_paddle.down, "S".lower())
# PADDLE TWO CONTROLS
screen.onkey(p2_paddle.up,"Up")
screen.onkey(p2_paddle.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # Put the ball in play
    ball.move()
    # Detect if ball has hit the top of the screen
    if ball.ycor() > 535 or ball.ycor() < -535:
        print('hit top wall')
        ball.change_direction_y() 
    # Detect if ball has hit right wall
    elif ball.xcor() >= 850 or ball.xcor() <= -850:
        game_on = False
    # Detect collision with right paddle
    elif ball.distance(p1_paddle) < 50 and ball.xcor() > 775 or ball.distance(p2_paddle) < 50 and ball.xcor() < -775:
        ball.change_direction_x()

screen.exitonclick()