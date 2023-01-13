import higherlowerlogo
import gamedata
import random
import emoji
import os

# Iterate through the list of individuals in game data and pass two options to the prompt for the user to choose.
def present_choices():
    options = 0
    for i, thing in enumerate(gamedata.data):
        dict_num = random.randint(0,49)
        new_dict = gamedata.data[dict_num]
        followers = new_dict['follower_count']
        name = new_dict['name']
        descr = new_dict['description']
        country = new_dict['country']
        options += 1
        if options == 1:
            print(f"Compare A: {name}, a {descr} from {country}.")
            print(higherlowerlogo.versus)
            a_followers = followers
        else:
            print(f"Against B: {name}, a {descr} from {country}.")
            b_followers = followers
        if options == 2:
            break
    return a_followers, b_followers

# Compare followings of each option
def compare_followings(option_a_followers,option_b_followers):
    if option_a_followers > option_b_followers:
        answer = "A"
    else:
        answer = "B"
    return answer

def higher_lower():
    current_score = 0
    game_on = True
    print(higherlowerlogo.logo)
    while game_on is True:
        # present choices and return follower count from game data
        a_followers, b_followers = present_choices()
        # Collect user input on whether option A or B:
        choice = input("Who has more followers? Type 'A' or 'B':").upper()
        # Compare user choices follower counts returned from present_choices function
        answer = compare_followings(a_followers, b_followers)
        if choice == answer:
            os.system('cls||clear')
            current_score +=1
            print(higherlowerlogo.logo)
            print(f"CORRECT! Your current score is {current_score}!! ",emoji.emojize(':thumbs_up:'))
            # Some code to make next comparison A == answer[index]
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_on = False
            break
higher_lower()