from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import sqlite3
import os

# Create a title screen and a "Start Game" & "End" option
# grow the snake each time it eats food
# randomize the location of the food
# If the snake hits itself or the edge of the screen, the snake dies and the game restarts
path = os.getcwd()
print(path)
os.chdir(path + "//Snake Game")

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Let's Play the Snake Game")
# tracer disables when value 0 is passed through
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

conn = sqlite3.connect('snakescores.db')
# Check existence of userdata table
if not scoreboard.check_table_exists(conn, ('scoredata',)):
    scoreboard.create_table()
conn.commit()
conn.close()

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
        scoreboard.user_scored()
        # print("found the food!")
        # recreate the food in another location and destroy the last piece of food
    # Add a piece to the snake after eating


screen.exitonclick()






