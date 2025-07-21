def pause():
    input("Press Enter to continue")

def main():
    print("\n=====================")
    print("= Simple Calculator =")
    print("=====================")

    while True:
        try:
            print("====== CHOICES ======")
            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 + num2
                print("Result: ", result)
                pause()
            elif choice == 2:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 - num2
                print("Result: ", result)
                pause()
            elif choice == 3:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = num1 * num2
                print("Result: ", result)
                pause()
            elif choice == 4:
                while True:
                    try:
                        num1 = int(input("Enter first number: "))
                        num2 = int(input("Enter second number: "))
                        result = num1 / num2
                        print("Result: ", result)
                        pause()
                        break
                    except ZeroDivisionError:
                        print("Invalid input. Cannot divide by zero.")
            elif choice == 5:
                print("Terminating calculator...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
