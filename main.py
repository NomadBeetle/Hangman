import random

from hangman_words import word_list
from hangman_art import logo, stages

lives = 6
chosen_word = random.choice(word_list)

print(logo)

Game_Over = False
placeholder = ["_"] * len(chosen_word)
print("Word to guess: " + "".join(placeholder))

while not Game_Over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input, Please Try again later.")
        continue

    if guess in placeholder:
        print(f"You have already guessed the letter '{guess}'. Try another letter.")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            placeholder[i] = guess

    if guess not in chosen_word:
        print(f"e.g. You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

    print(stages[lives])

    display = "".join(placeholder)
    print("Word to guess: " + display)

    if "_" not in placeholder:
        print("**************************** YOU WIN ****************************")
        Game_Over = True

    if lives == 0:
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
        Game_Over = True
