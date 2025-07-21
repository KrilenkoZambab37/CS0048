# If the program does not run on its own, run it in mp1compile.py
# def main() makes the program only run in mp1compile.py where it is being called

import os

def pause():
    input("Press Enter to continue")
def main():
    steps = 0
    calories = 0
    while True:
        os.system('cls' if os.name =='nt' else 'clear')

        print("\n--- Fitness Tracker ---\n")
        print("1. Add steps")
        print("2. View total steps")
        print("3. View calories burned")
        print("4. Exit")
        choice = input("\nPlease enter your choice: ")

        if choice == "1":
            newstep = int(input("Please enter an amount: "))
            steps += newstep
            pause()
        elif choice == "2":
            print("--- ---")
            print("Total steps taken: ", steps)
            pause()
        elif choice == "3":
            calories = steps * 0.04
            print(f"Total calories burned: {calories:1f} cal")  #bruh why it no format
            pause()                                             #shows 6 decimal places instead of 1
        elif choice == "4":
            print("Keep moving! Movement is life! Goodbye.")
            break
        else:
            print("Invalid input. Please try again.")
            pause()
