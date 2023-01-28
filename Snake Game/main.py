from turtle import Turtle, Screen
import time
from snake import Snake

# Create a title screen and a "Start Game" & "End" option
# grow the snake each time it eats food
# randomize the location of the food
# If the snake hits itself or the edge of the screen, the snake dies and the game restarts

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Let's Play the Snake Game")
# tracer disables when value 0 is passed through
screen.tracer(0)

snake = Snake()

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


screen.exitonclick()






