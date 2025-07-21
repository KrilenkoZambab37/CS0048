#menu framework

import number_game
import simple_calc
import grade_calc
import temp_conv
import todo_list
import os

def pause():
    input("Press Enter to continue")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("\n=====================")
print("=     MAIN MENU     =")
print("=====================")

while True:
    try:
        print("====== CHOICES ======")

        print("\n1. Simple Calculator")
        print("2. Temperature Converter")
        print("3. To-do list")
        print("4. Number Game")
        print("5. Student Grade Calculator")
        print("6. Exit")

        print("")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            simple_calc.main()
            pause()
            clear()
        elif choice == 2:
            temp_conv.main()
            pause()
            clear()
        elif choice == 3:
            todo_list.main()
            pause()
        elif choice == 4:
            number_game.main()
            pause()
        elif choice == 5:
            grade_calc.main()
            pause()
        elif choice == 6:
            print("Terminating program... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please try again.")
