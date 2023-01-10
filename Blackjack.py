import random

blackjack_limit = 21


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_scores(cards):
    score = sum(cards)
    return score

def another_card(players_score,dealers_score):
    new_player_card = random.choice(cards)
    if new_player_card == 11 and players_score == 20:
        new_player_card == 1
    if dealers_score >= 17 and dealers_score <=21:
        dealer_new_card = 0
    else:
        dealer_new_card = random.choice(cards)
        if dealer_new_card == 11 and dealers_score == 20:
            dealer_new_card == 1
    return new_player_card, dealer_new_card

def print_the_hands(players_cards,dealers_cards):
    players_score = sum(players_cards)
    print("Your current hand: ", players_cards, "Current score: ", players_score)
    print("Dealers first card: ", dealers_cards[0])
# def check_scores():

# Need to write a function that if the players next card is an 11, and their score is also pushed above 21
# convert it to a 1. If the score still goes over 21, player busts.
start_game = input("Would you like to start the blackjack game? Type 'y' or 'n': ")
spin_up = True
while spin_up is True:
    if start_game == 'y':
        # Initialize variables for game
        players_score = 0
        dealers_score = 0
        players_cards = []
        dealers_cards = []
        # Deal out the first two cards and show the player their score
        for i, card in enumerate(cards):
            if i >= 2:
                break
            else:
                players_cards.append(random.choice(cards))
                dealers_cards.append(random.choice(cards))
        # Determine whether a blackjack was drawn by either the player or dealer
        if 10 and 11 in players_cards:
            print("Player Blackjack! Congratulations!")
            bust_flag = False
            dealer_limit = False
            break
        elif 10 and 11 in dealers_cards:
            print("Dealer Blackjack! Sorry, player loses!")
            bust_flag = False
            dealer_limit = False
            break
        elif 10 and 11 in dealers_cards and 10 and 11 in players_cards:
            print("WOW! Double Blackjack! However the Dealer Wins in this case!")
            bust_flag = False
            dealer_limit = False
            break
        # calculate the scores and print them out
        players_score = calculate_scores(players_cards)
        dealers_score = calculate_scores(dealers_cards)
        print_the_hands(players_cards,dealers_cards)
        bust_flag = True
        while bust_flag is True:
            if players_score <= 21:
                # let the player draw cards until they bust or until they no longer want more cards.
                another = input("Type 'y' to get another card, type 'n' to pass: ")
                if another == 'y':
                    new_player_card, new_dealer_card = another_card(players_score,dealers_score)
                    players_cards.append(new_player_card)
                    dealers_cards.append(new_dealer_card)
                    players_score = calculate_scores(players_cards)
                    dealers_score = calculate_scores(dealers_cards)
                    print_the_hands(players_cards,dealers_cards)
                # If the player is done drawing cards, let the computer play now.
                elif another == 'n':
                    dealer_limit = True
                    while dealer_limit is True:
                        if dealers_score >= 17:
                            dealer_limit = False
                            break
                        elif dealers_score <= 16:
                            dealers_cards.append(random.choice(cards))
                            dealers_score = calculate_scores(dealers_cards)
                    # Compare the player and dealers scores and send appropriate messages
                    if players_score > dealers_score:
                        print('Congratulations, you won the hand!')
                        print("Your score: ", players_score, "Your hand: ", players_cards)
                        print("Dealers score: ", dealers_score, "Dealers Cards: ", dealers_cards)
                    elif dealers_score > players_score and dealers_score < 22:
                        print('Sorry, looks like you lost to the dealers hand.')
                        print("Your score: ", players_score, "Your hand: ", players_cards)
                        print("Dealers score: ", dealers_score, "Dealers Cards: ", dealers_cards)
                    elif dealers_score == players_score:
                        print('Looks like it was a Draw!')
                        print("Your score: ", players_score, "Your hand: ", players_cards)
                        print("Dealers score: ", dealers_score, "Dealers Cards: ", dealers_cards)
                    else:
                        print("Dealer busts. Player wins!")
                        print("Your score: ", players_score, "Your hand: ", players_cards)
                        print("Dealers score: ", dealers_score, "Dealers Cards: ", dealers_cards)
                    bust_flag = False
                    break
            else: 
                print("Your score went above 21, you bust!")
                bust_flag = False
                break
    play_again = input("Would you like to play again? Enter 'y' or 'n': ")
    if play_again == 'n':
        spin_up = False
        break
    elif play_again == 'y':
        bust_flag = True
        dealer_limit = True