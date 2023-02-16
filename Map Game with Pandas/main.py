from turtle import Turtle, Screen
import pandas as pd

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data['state'].tolist()

correct_guesses = []
num_correct = 0
while num_correct < 52:
    user_answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    if user_answer in states:
        correct_guesses.append(user_answer)
        num_correct += 1
        index = int(data[data['state'] == user_answer].index.values)
        print(index, type(index))
        x_pos = data.loc[index].at['x']
        y_pos = data.loc[index].at['y']
        # print('xpos is: ', x_pos, 'y pos is: ', y_pos)
        turtle.penup()
        turtle.goto((x_pos,y_pos))
        turtle.write(user_answer, font=('Arial',8,'normal'))



screen.exitonclick()