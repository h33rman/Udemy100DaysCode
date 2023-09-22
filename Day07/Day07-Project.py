# HANG AN game
import hangman_art
import hangman_words


word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo


import random
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
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        UserLives -= 1
        print(stages[UserLives])
        if UserLives == 0:
            GameStatus = True
            print("You lose")
    if "_" not in display:
        GameStatus = True
        print("You win")
    print(display)


