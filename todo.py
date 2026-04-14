# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file]
except FileNotFoundError:
    tasks = []
    # Save tasks to file
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")
tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed:", removed)
        else:
            print("Invalid number")
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")