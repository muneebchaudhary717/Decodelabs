# -------------------------------
# TO-DO LIST PROGRAM
# -------------------------------

tasks = []   # List to store tasks
task_id = 1  # Unique ID for each task


def add_task():
    global task_id
    task_name = input("Enter task: ")

    # Dictionary (like database row)
    task = {
        "id": task_id,
        "name": task_name
    }

    tasks.append(task)   # INSERT
    print("Task added successfully!\n")

    task_id += 1


def add_task_api(task_name: str):
    """Add a task programmatically (for web API). Returns the created task dict."""
    global task_id
    task = {"id": task_id, "name": task_name}
    tasks.append(task)
    task_id += 1
    return task


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        print(f"ID: {task['id']} | Task: {task['name']}")
    print()


def get_tasks_api():
    """Return list of tasks for API usage."""
    return tasks


def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.\n")
        return

    try:
        tid = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == tid:
                tasks.remove(task)
                print("Task deleted successfully!\n")
                return

        print("Task ID not found.\n")

    except ValueError:
        print("Invalid input! Enter a number.\n")


def delete_task_api(tid: int) -> bool:
    """Delete task by id for API usage. Returns True if deleted."""
    for task in tasks:
        if task["id"] == tid:
            tasks.remove(task)
            return True
    return False


def update_task():
    if len(tasks) == 0:
        print("No tasks to update.\n")
        return

    try:
        tid = int(input("Enter task ID to update: "))

        for task in tasks:
            if task["id"] == tid:
                new_name = input("Enter new task name: ")
                task["name"] = new_name
                print("Task updated successfully!\n")
                return

        print("Task ID not found.\n")

    except ValueError:
        print("Invalid input! Enter a number.\n")


def update_task_api(tid: int, new_name: str) -> bool:
    """Update task name by id for API usage. Returns True if updated."""
    for task in tasks:
        if task["id"] == tid:
            task["name"] = new_name
            return True
    return False


# -------------------------------
# MAIN PROGRAM (IPO MODEL)
# -------------------------------

if __name__ == "__main__":
    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            update_task()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.\n")
