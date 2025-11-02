# Simple To-Do List Manager

tasks = [] 

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == '3':
        if not tasks:
            print("No tasks to mark.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = tasks[task_num - 1] + " ✅"
                print("Task marked as complete!")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
