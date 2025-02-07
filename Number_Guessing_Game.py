import random

def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    while True:
        try:
            lower = int(input("Enter the lower bound: "))
            upper = int(input("Enter the upper bound: "))
            if lower >= upper:
                print("Lower bound must be less than upper bound. Try again.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers for bounds.")
    
    number = random.randint(lower, upper)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1
            
            if guess < lower or guess > upper:
                print(f"Out of bounds! Guess a number between {lower} and {upper}.")
            elif guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ["yes", "y"]:
            number_guessing_game()
        elif play_again in ["no", "n"]:
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    number_guessing_game()
