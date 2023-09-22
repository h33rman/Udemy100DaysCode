# HANG AN game
from hangman_art import stages, logo
from hangman_words import word_list
import random
import os

def clear():
    os.system('clear')

chosen_word = random.choice(word_list)

display = []

for letter in range(len(chosen_word)):
    display.append("_")

print(display)

UserLives = 6
GameStatus = False

print(logo)

while GameStatus==False:
    
    guess = input("Guess a letter: ").lower()
    clear()
    
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        UserLives -= 1
        print(stages[UserLives])
        if UserLives == 0:
            GameStatus = True
            print("You lose")

    if "_" not in display:
        GameStatus = True
        print("You win")
    print(display)


