tasks = []
def display_menu():
    print("\n---- To-Do List Menu ----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{i}. {task['description']} - [{status}]")

def add_task():
    task_description = input("\nEnter task description: ")
    tasks.append({"description": task_description, "completed": False})
    print(f"Task '{task_description}' added!")

def update_task():
    view_tasks()
    task_num = int(input("\nEnter the task number to update: "))

    if 1 <= task_num <= len(tasks):
        task = tasks[task_num - 1]
        print(f"1. Mark '{task['description']}' as complete")
        print(f"2. Edit description")
        choice = input("Choose option (1 or 2): ")

        if choice == '1':
            task['completed'] = True
            print(f"Task '{task['description']}' marked as complete!")
        elif choice == '2':
            new_description = input("Enter new description: ")
            task['description'] = new_description
            print(f"Task updated to '{new_description}'")
        else:
            print("Invalid option.")
    else:
        print("Invalid task number.")
        
def delete_task():
    view_tasks()
    task_num = int(input("\nEnter the task number to delete: "))

    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['description']}' deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
