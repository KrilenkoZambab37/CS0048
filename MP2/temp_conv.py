def pause():
    input("Press Enter to continue")

def main():
    print("=========================")
    print("= Temperature Converter =")
    print("=========================")

    while True:
        try:
            print("======== CHOICES ========")
            print("\n1. Fahrenheit to Celsius")
            print("2. Celsius to Fahrenheit")
            print("3. Exit")

            choice = int(input("Enter choice: "))
            if choice == 1:
                celc = int(input("Enter temperature (In C°): "))
                temp = ((celc * 9 / 5) + 32)
                print("Result: ", temp, " F°")
                pause()
            elif choice == 2:
                fahr = int(input("Enter temperature (In F°): "))
                celc = ((fahr - 32) * 5 / 9)
                print("Result: ", celc, " C°")
                pause()
            elif choice == 3:
                print("Terminating converter... Thank you!")
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
