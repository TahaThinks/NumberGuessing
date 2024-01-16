import random
from art import logo

print(logo)
print("Welcome to the Guessing Game")
print("I am thinking of a Number between 1 & 100")
selected_number = random.randint(1,100)
print(selected_number)


def guess(attempts):
    if attempts > 0:
        print(f"You entered the Function, you have {attempts} attempts")
        user_guess = int(input("Make a Guess: "))
        if user_guess < selected_number:
            print("Too Low.\nGuess again.")
            guess(attempts-1)
        elif user_guess > selected_number:
            print("Too High.\nGuess again.")
            guess(attempts-1)
        elif user_guess == selected_number:
            print("Your Guess is Correct")
    else:
        print(f"You Lost, the correct number is {selected_number}")


user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if user_difficulty == "e":
    print("You Selected Easy")
    guess(10)
else:
    print("You Selected Hard")
    guess(5)

