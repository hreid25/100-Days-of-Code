import higherlowerlogo
import gamedata
import random
import emoji
import os

# Compare followings of each option
def compare_followings(option_a_followers,option_b_followers):
    if option_a_followers > option_b_followers:
        answer = "A"
    else:
        answer = "B"
    return answer

def generate_account():
    dict_num = random.randint(0,49)
    new_dict = gamedata.data[dict_num]
    return new_dict

def game_continues(account_a,account_b):
    account_a = account_b
    account_b = generate_account()
    # print("game continues!", account_a,account_b)
    return account_a, account_b

def higher_lower():
    current_score = 0
    game_on = True
    print(higherlowerlogo.logo)
    while game_on is True:
        # Grab random accounts
        if current_score < 1 :
            account_a = generate_account()
            account_b = generate_account()
        # Present choices and return follower count from game data
        print(f"Compare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}.")
        print(higherlowerlogo.versus)
        print(f"Against B: {account_b['name']}, a {account_b['description']} from {account_b['country']}.")
        choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        # Compare follower count of each account
        answer = compare_followings(account_a['follower_count'], account_b['follower_count'])
        if choice == answer:
            game_on = True
            current_score +=1
            os.system('cls||clear')
            print(higherlowerlogo.logo)
            print(f"CORRECT! Your current score is {current_score}!! ",emoji.emojize(':thumbs_up:'))
            account_a, account_b = game_continues(account_a, account_b)
        else:
            game_on = False
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break
        
higher_lower()

