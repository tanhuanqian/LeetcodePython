import json
import os
import sys

# Define the filename for storing tasks
TASKS_FILE = 'tasks.json'

# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(description):
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo'
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

# Function to update a task
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(updated_tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task deleted successfully (ID: {task_id})")

# Function to mark a task as 'in progress' or 'done'
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            save_tasks(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return
    print("Task not found.")

# Function to list tasks based on their status or list all
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
        if filtered_tasks:
            for task in filtered_tasks:
                print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
        else:
            print(f"No tasks with status '{status}'.")
    else:
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
        else:
            print("No tasks available.")

# Main function to handle command line arguments
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli [command] [arguments]")
        return

    command = sys.argv[1].lower()

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: task-cli add [description]")
            return
        add_task(sys.argv[2])
    
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update [id] [description]")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: task-cli delete [id]")
            return
        delete_task(int(sys.argv[2]))

    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress [id]")
            return
        mark_task(int(sys.argv[2]), 'in-progress')
    
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done [id]")
            return
        mark_task(int(sys.argv[2]), 'done')
    
    elif command == 'list':
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
