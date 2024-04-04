# Guess the number 1 to 100
import random

# choose the level of difficulty
# easy: 10 attempts
EASY_ATTEMPTS = 10
# medium: 5 attempts
MEDIUM_ATTEMPTS = 5
# hard: 3 attempts
HARD_ATTEMPTS = 3


# ask the player to choose a difficulty
def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")
    if difficulty == 'easy':
        return EASY_ATTEMPTS
    elif difficulty == 'medium':
        return MEDIUM_ATTEMPTS
    elif difficulty == 'hard':
        return HARD_ATTEMPTS
    else:
        return 0


# let the player guess a number
def check_answer(guess,number,turns):
    """
    Check answer against guess. 
    Return the number of turns remaining.
    """
    if guess < number:
        print("Too low.")
        return turns - 1
    elif guess > number:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}.")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)

    turns = choose_difficulty()

    print(f"You have{turns} attempts remaining to guess the number.")

    game_over = False

    while not game_over:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            game_over = True

        elif guess == number:
            game_over = True
            
        elif guess != number:
            print("You have", turns, "attempts remaining.")
            print("Guess again.")

game()