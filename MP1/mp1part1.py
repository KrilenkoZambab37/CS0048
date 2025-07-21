# If the program does not run on its own, run it in mp1compile.py
# def main() makes the program only run in mp1compile.py where it is being called

import os

def pause():
    input("Press Enter to continue")
def main():
    total = 0
    while True:
        os.system('cls' if os.name =='nt' else 'clear')

        print("\n--- Welcome to Python Restaurant ---")
        print("--- Your choice ---")
        print("1. Burger - ₱120")
        print("2. Pizza - ₱300")
        print("3. Pasta - ₱250")
        print("4. Fries - ₱80")
        print("5. Exit")
        choice = input("Please select your order: ")

        if choice == "1":
            #add burger variations
            print("Added 1 Burger to your order.")
            total += 120
            pause()
        elif choice == "2":
            #add pizza sizes
            print("Added 1 Pizza to your order.")
            total += 300
            pause()
        elif choice == "3":
            #maybe add choices for different pasta options
            print("Added 1 Pasta to your order.")
            total += 250
            pause()
        elif choice == "4":
            #maybe add choices for S, M, or L fries
            print("Added 1 Fries to your order.")
            total += 80
            pause()
        elif choice == "5":
            print("Thank you for dining at our restaurant.")
            break
        else:
            print("Invalid input, please try again.")
            pause()

    print("\n--- Order Summary ---")
    print("\nTotal before discount: ₱", total)
    if total > 500:
        print("Your order exceeds ₱500. A 10% discount has been applied")
        discount = total * 0.10
        total -= discount
    print(f"Final amount to pay:   ₱{int(total)}")
