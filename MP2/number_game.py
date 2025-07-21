import random

def pause():
    input("Press Enter to continue")

def main():
    print("\n======================")
    print("=  Guess  A  Number  =")
    print("======================")
    while True:
        try:
            print("======  CHOICES ======")
            print("\n1. Play Number Guessing Game")
            print("2. Exit")

            choice = int(input("Enter your choice (1-2): "))
            if choice == 1:
                number = random.randint(1, 100)
                attempts = 0

                print("\nI'm thinking of a number between 1 and 100...")

                while True:
                    try:
                        guess = int(input("Guess the number: "))
                        attempts += 1

                        if guess < 1 or guess > 100:
                            print("Out of bounds! Try a number between 1 and 100.")
                        elif guess < number:
                            print("Too low!")
                        elif guess > number:
                            print("Too high!")
                        else:
                            print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            elif choice == 2:
                print("Terminating... Goodbye!")
                break
            else:
                print("Invalid choice. Enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
