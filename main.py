from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guess_number(mystery, guess, turn):
    """Checks answer against guess, returns the number of turns remaining."""
    if mystery>guess:
        print("Too low.")
        return turn -1
    elif mystery<guess:
        print("Too high.")
        return turn - 1
    else:
        print(f"You got it! The answer was {mystery}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mystery_number = randint(1, 100)

    turns = set_difficulty()


    guessed = 0
    while guessed != mystery_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guessed = int(input("Make a guess: "))
        turns = guess_number(mystery=mystery_number, guess=guessed, turn=turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()






