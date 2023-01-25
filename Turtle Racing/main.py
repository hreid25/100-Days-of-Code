from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

# Instantiate all players, set their colors and positions
def create_turtle_starts(num_turtles):
     x = -225
     y = -100
     for participant in range(num_turtles):
          print(participant)
          turtle_id = int(participant)
          turtle_player = Turtle(shape="turtle")
          turtle_player.color(str(colors[participant]))
          if int(participant) > 0:
               y += 50
          turtle_player.penup()
          turtle_player.goto(x,y)

create_turtle_starts(6)
player_list = [i for i in screen.turtles()]

if user_bet:
     is_race_on = True

while is_race_on:
     for player in player_list:
          random_distance = random.randint(0,10)
          player.forward(random_distance)
          if player.xcor() > 230:
               if user_bet == player.color():
                    print("Congrats, you won nothing!")
               else:
                    print("Sorry, you guessed wrong and lost everything.")
               print(player.color())
               is_race_on = False
               break


# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def move_counterclockwise():
#      tim.left(10)

# def move_clockwise():
#      tim.right(10)

# def clear_screen_reset():
#      screen.resetscreen()
     
# screen.listen()

# # screen.onkey(key="space", fun=move_forwards)
# screen.onkey(key="A".lower(), fun=move_counterclockwise)
# screen.onkey(key="D".lower(), fun=move_clockwise)
# screen.onkey(key="S".lower(), fun=move_backwards)
# screen.onkey(key="W".lower(), fun=move_forwards)

# screen.onkey(key="C", fun=clear_screen_reset)

screen.exitonclick()

#  Passing functions to a function will be useful when listening for events.