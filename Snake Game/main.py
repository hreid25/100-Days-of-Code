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

user = screen.textinput("Enter your player name!", "Please enter your name: ")

db = User(user)
get_high_score = db.get_high_score()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.post_scoreboard(0,270)
high_scoreboard = Scoreboard()
high_scoreboard.post_high_score(get_high_score,0,240)

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
        snake.extend_snake()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
        db.insert_score(scoreboard.score)
    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
            db.insert_score(scoreboard.score)
    # if head collides with any segment in the tail:
        # trigger game over sequence.


screen.exitonclick()






