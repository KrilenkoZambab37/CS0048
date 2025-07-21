# If the program does not run on its own, run it in mp1compile.py
# def main() makes the program only run in mp1compile.py where it is being called

import os
global cart
cart = ""

def pause():
    input("\nPress Enter to continue")

def add_to_cart():
    global cart

    itemname = input("Enter item to add: ").strip().capitalize()
    try:
        itemquantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Must be a number.")
        return

    if itemquantity < 1:
        print("Quantity must be at least 1.")
        return

    if itemname == "Rice":
        price = 50
    elif itemname == "Eggs" or itemname == "Egg":
        price = 7
        itemname = "Eggs"
    elif itemname == "Milk":
        price = 60
    elif itemname == "Bread":
        price = 35
    else:
        print("Invalid item")
        return

    itemtotal = price * itemquantity
    print(f"Added {itemquantity} {itemname}(s) to cart.")
    cart += f"{itemname} x {itemquantity} = {itemtotal}\n"


def checkout():
    if cart == "":
        print("Cart is empty.")
        return

    print("\n--- Cart Summary ---")
    total = 0
    
    for line in cart.splitlines():
        itemtotal = int(line.split('=')[1].strip().split()[0])
        total += itemtotal

    print(cart)
    vat = round(total * 0.12, 2)
    total = round(total + vat, 2)
    print("Subtotal: ₱" + str(total))
    print(f"VAT (12%): ₱{vat:.2f}")
    print("Total: ₱ " + str(vat + total) + '\n')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n--- Grocery Store ---")
        print("1. View Items")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\n• Rice: ₱50")
            print("• Eggs: ₱7")
            print("• Milk: ₱60")
            print("• Bread: ₱35")
            pause()
        elif choice == "2":
            add_to_cart()
            pause()
        elif choice == "3":
            checkout()
            pause()
        elif choice == "4":
            print("Thank you for shopping! - R")
            break
        else:
            print("Invalid choice. Please try again.")
            pause()
