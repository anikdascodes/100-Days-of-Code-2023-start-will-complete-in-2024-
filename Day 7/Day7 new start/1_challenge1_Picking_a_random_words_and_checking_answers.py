# Step 1

word_list = ["ardvark", "baboon", "camel"]

#TODO 1 : randomly choose a word from the word_lists and assign it  to a variable called chosen_word. 

import random

chosen_word = random.choice(word_list)

#TODO 2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO 3 : Check if the letter the user guessed (guess) lowercase. 

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Worng")