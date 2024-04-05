import random

# choose the level of difficulty
EASY_ATTEMPTS = 10
MEDIUM_ATTEMPTS = 5
HARD_ATTEMPTS = 3

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

def check_answer(guess, number):
    """
    Check answer against guess. 
    Return True if guess is correct.
    """
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {number}.")
        return True
    return False

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)

    attempts = choose_difficulty()
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts -= 1
        if check_answer(guess, number):
            break
        
        print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")

game()
