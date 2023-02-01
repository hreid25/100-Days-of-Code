from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from user import User

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Let's Play the Snake Game")
# tracer disables when value 0 is passed through
screen.tracer(0)

# user = screen.textinput("Enter your player name!", "Please enter your name: ")
# db = User(user)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with Food
    if snake.head.distance(food) < 16.5:
        food.touched_food()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    # Add a piece to the snake after eating


screen.exitonclick()






