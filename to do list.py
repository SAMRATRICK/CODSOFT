#!/usr/bin/env python
# coding: utf-8

# In[1]:


# To-Do List Program in Python

# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found.")

# Function to show all tasks in the list
def show_tasks():
    print("Tasks in the to-do list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Main function to interact with the user
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()


# In[ ]:




