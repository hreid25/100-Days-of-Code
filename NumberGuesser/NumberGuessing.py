import random
import numberguessinglogo

def is_guess_correct(guesses_left,answer):
    while guesses_left >= 1:
        guess = int(input("Make a guess: "))
        if guess != answer:
            if guess < answer:
                print("Too low.\nGuess again.")
            else:
                print("Too high.\nGuess again.")
            print(f"You have {guesses_left - 1} attempts remaining to guess the number.")
            guesses_left -= 1
        else:
            print(f"You got it! The answer was {answer}.")
            break
            
def number_guessing_game():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty by typing either 'easy' or 'hard': ")
    answer = int(random.choice(range(1,100)))
    print("Pssst, the correct answer is: ", answer)
    if difficulty == "easy":
        print("You have 10 attempts remaining to guess the number")
        is_guess_correct(10,answer)
    else:
        print("You have 5 attempts remaining to guess the number")
        is_guess_correct(5, answer)

print(numberguessinglogo.logo)
number_guessing_game()

# print("You have run out of guesses! Would you like to restart the game?")
# try_again = input("Enter 'y' or 'n'.")
# if try_again == 'y':