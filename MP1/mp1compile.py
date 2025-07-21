import mp1part1
import mp1part3
import mp1part2

import os

def pause():
    input("Press Enter to continue")

while True:
    os.system('cls' if os.name =='nt' else 'clear')

    print("\n---[ Machine Problem 1-3 Compiled ]---\n")
    print("1. Restaurant Order Management System")
    print("2. Grocery Store Management System")
    print("3. Fitness Tracker")
    print("4. Exit")

    choice = input("\nPlease enter your choice: ")

    if choice == "1":
        mp1part1.main()
        pause()
    elif choice == "2":
        mp1part2.main()
        pause()
    elif choice == "3":
        mp1part3.main()
        pause()
    elif choice == "4":
        print("\nThank you for using my program.")
        print("\nTerminating ...")
        break
    else:
        print("Invalid input. Please try again.")
