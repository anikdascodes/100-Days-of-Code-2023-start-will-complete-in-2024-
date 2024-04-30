from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
# Function to check user's guess against actual answer .
def check_answer(guess, answer, turns):
    """Check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High.")
        return turns -1
        turns -= 1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")


# Make a function to set difficulty. 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        




def game():
    print(logo)
    # Choose a ramdom number  between 1 and 100. 

    print("Welcome to the Number Gussing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")


    turns = set_difficulty()
    

    # Repeat the guessing functionality if they get it wrong. 
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remainings to guess the number.")

        # Let the user guess a number . 
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

# Track the number of turns and reduce by 1 if they get it wrong . 


 


