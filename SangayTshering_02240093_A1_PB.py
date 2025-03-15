import random

def guess_number_game():
    """Number Guessing Game"""
    print("\nHere is a Number Guessing Game to Kill Your Boredom!")
    lower = 1
    upper = 20
    computer_number = random.randint(lower, upper)

    print(f"Guess a number between {lower} and {upper}.")

    attempts = 0

    while True:
        """Output"""
        try:
            guess = int(input("Enter your Guess: "))
            attempts += 1
            if guess < lower or guess > upper:
                print(f"Please guess a number between {lower} and {upper}.")
            elif guess < computer_number:
                print("Low! Try guessing a higher number.")
            elif guess > computer_number:
                print("High! Try guessing a lower number.")
            else:
                print(f"WOW! You have guessed the number {computer_number} correctly in {attempts} attempts")
                break
        except ValueError:
            print("Invalid Input! Please enter a valid number")

def rock_paper_scissors_game():
    """Rock Paper Scissors Game"""
    print("\nHere is a Rock, Paper, Scissors Game!")
    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose 'rock', 'paper' or 'scissors' (or enter 'exit' to go back to the menu): ").lower()

        if user_choice == "exit":
            break

        if user_choice not in options:
            print("Choice Invalid! Please choose between 'rock','paper or 'scissors'.")
            continue

        computer = random.choice(options)
        print(f"Compuer Chose: {computer}")

        """Output"""
        if user_choice == computer:
            print ("It's a tie!")
        elif (user_choice == "rock" and computer == "scissors"):
            print("Rock beats Scissors, You Win!")
        elif (user_choice == "paper" and computer == "rock"):
            print("Paper Beats Rock, You Win!")
        elif (user_choice == "scissors" and computer == "paper"):
            print("Scissors Beats Paper, You Win!")
        else:
            print("Upps, You lose!")
        
def display_menu():
    """Menu"""
    print("\nSelect a Game to Play:")
    print("1. Number Guessing Game")
    print("2. Rock Paper Scissors Game")
    print("3. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))

            if choice == 1:
                guess_number_game()
            elif choice == 2:
                rock_paper_scissors_game()
            elif choice == 3:
                print("You are Exiting the Program.")
                break
            else:
                print("Invalid choice! Please select a Number between 1 to 3")
        except ValueError:
            print("Invalid Input! Please enter a valid number.")

if __name__ == "__main__":
    main()


