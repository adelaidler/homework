
# https://www.scaler.com/topics/rock-paper-scissors-python/

import random
from enum import IntEnum

class Action(IntEnum):
    Rock, Paper, Scissors = 0, 1, 2

# function to take input from the user for Rock paper scissors python code
def get_user_action():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    user_choice = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(user_choice)
    return action

# function to decide the program's choice for the Rock paper scissors python code
def get_program_action():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

# function to determine winner for Rock paper scissors python code
def determine_winner(user_choice, program_choice):
    if user_choice == program_choice:
        print(f"Both players selected {user_choice.name}. It's a tie!")
    elif user_choice == Action.Rock:
        if program_choice == Action.Scissors:
            print("You win! because Rock smashes scissors.")
        else:
            print("You lose :( Paper covers rock!")
    elif user_choice == Action.Paper:
        if program_choice == Action.Rock:
            print("You win! because Paper covers rock.")
        else:
            print("You lose :( Scissors cuts paper!")
    elif user_choice == Action.Scissors:
        if program_choice == Action.Paper:
            print("You win! because Scissors cuts paper.")
        else:
            print("You lose :( Rock smashes scissors!")


# Rock paper scissors python code
while True:
    try:
        user_choice = get_user_action()
    except ValueError as e:
        # user enter value not in valid range
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        # ask user to re-enter the choice
        continue

    # determine the program's input (randomly selected)
    program_choice = get_program_action()

    # determine and display the winner
    determine_winner(user_choice, program_choice)

    # Ask the user whether they want to play again.
    play_again = input("Play again? (y/n): ")
    # End the game, if the user input is not 'y'
    if play_again.lower() != "y":
        break





