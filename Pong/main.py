from turtle import Turtle, Screen
from divider import Divider
from ball import Ball
from scoreboard import create_scoreboard
from paddles import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
# Create ball
ball = Ball()
# Create Dividing line
divide_screen = Divider()
# Initialize player score displays
p1_score = create_scoreboard((-200,200))
p2_score = create_scoreboard((150,200))
# Initialize player paddles
p1_paddle = Paddle((-350,0))
p2_paddle = Paddle((350,0))
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
    time.sleep(0.05)
    screen.update()
    # Put the ball in play
    ball.move()
    print(ball.xcor(),ball.ycor())
    # print(ball.distance(p2_paddle),ball.xcor())
    # Detect if ball has hit the top or bottom of the screen
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.change_direction_y() 
    # Detect collision with right paddle
    if ball.distance(p2_paddle) < 50 and ball.xcor() > 330 or ball.distance(p1_paddle) < 50 and ball.xcor() < -330: 
        print("Made Contact")
        ball.change_direction_x()
    # Detect if ball has hit right wall
    if ball.xcor() > 390 or ball.xcor() <= -390:
        if ball.xcor() <= -390:
            p1_score.score += 1
            p1_score.update_scoreboard()
        if ball.xcor()>390:
            p2_score.score += 1
            p2_score.update_scoreboard()
        ball.goto(0,0)
        ball.change_direction_x()
        ball.move()
        

screen.exitonclick()