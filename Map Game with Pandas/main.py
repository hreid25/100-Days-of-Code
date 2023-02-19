import turtle
import pandas as pd
from create_state import state_obj

# turtle = Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("50_states.csv")
states_list = state_data['state'].tolist()

correct_guesses = []

while len(correct_guesses) < 50:
    user_answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if user_answer == 'Exit':
        break
    if user_answer in states_list:
        correct_guesses.append(user_answer)
        index = int(state_data[state_data['state'] == user_answer].index.values)
        x_pos = state_data.loc[index].at['x']
        y_pos = state_data.loc[index].at['y']
        state_name_obj = state_obj(x_pos,y_pos, user_answer)

# produce a csv containing the states the user did not guess correctly and write them to a csv file

for i, state in enumerate(correct_guesses):
    if state in states_list:
        states_list.remove(state)

state_dict = {
    "States" : states_list
}

state_list_df = pd.DataFrame(states_list)
state_list_df.to_csv('states_to_learn.csv')

screen.exitonclick()