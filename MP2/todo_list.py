def main():
    tasks = []

    print("\n=====================")
    print("= Your To-do List =")
    print("=====================")

    while True:
        try:
            print("====== CHOICES ======")
            print("\n1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Exit")
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                task = input("Enter the task to add: ").strip()
                if task:
                    tasks.append(task)
                    print("Task added.")
                else:
                    print("Task cannot be empty.")
            elif choice == 2:
                if not tasks:
                    print("No tasks to remove.")
                    continue
                print("\nCurrent Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Task '{removed}' removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == 3:
                if tasks:
                    print("\nCurrent/Active Tasks:")
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks added yet.")
            elif choice == 4:
                print("Terminating the list... Thank you!")
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
