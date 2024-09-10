"""
task: View Task
cause: looping the rename method
"""

import datetime
import os
import subprocess
import time
import pyautogui

print(datetime.datetime.now())
print(datetime.datetime.today())

direction = os.getcwd()

# Create Directory for Todo
todo_dir = fr"{direction}\Todo_app"
try:
    os.mkdir(todo_dir)
except OSError:
    pass


# Function to put all the files list into it
def get_files_list():
    """Helper function to get the current list of tasks."""
    return os.listdir(todo_dir)


# Function to add a task.
def add_task():
    files_list = get_files_list()  # Refresh files list
    for i, file in enumerate(files_list, start=1):
        print(f"{i} => {file}")
    task = input("Task name: ")
    if task in files_list:
        print("The task file already exists.")
        q2 = input("Do you want to open it?\n$ ").lower()
        if q2 in ("yes", "y"):
            subprocess.Popen(["notepad.exe", fr"{todo_dir}\{task}"])
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'end')
        else:
            print("Back...")
            time.sleep(1)
    else:
        new_file = fr"{todo_dir}\{task}"
        with open(new_file, "w", encoding="utf-8") as nf:
            nf.write("New file has been created as '" + task + "'.\n")
        q1 = input("Do you want to write in your new task file?\n$ ").lower()
        if q1 == "yes":
            try:
                with open(new_file, "a", encoding="utf-8") as file:
                    file.write(f"# New file named by {task}\n")
                subprocess.Popen(["notepad.exe", new_file])
                pyautogui.hotkey('ctrl', 'end')
                print(f"-{task} has been added Successfully.")
            except FileNotFoundError as E:
                print(f"Error => {E}")
        else:
            print("Back...")
            time.sleep(1)


# Function to view a task
def view_task():
    files_list = get_files_list()  # Refresh files list
    # Printing the tasks
    if len(files_list) > 0:
        for i, file in enumerate(files_list, start=1):
            print(f"[#{i}] => {file}")

        # Renaming tasks
        rename_file = input("Do you want to rename a file? (yes/y or no/n): \n$ ").strip().lower()
        if rename_file in ("yes", "y"):
            task_to_rename = input("Old task name: ").strip().lower()
            lower_files_list = [file.lower() for file in files_list]
            if task_to_rename in lower_files_list:
                new_name = input("Task new name: ").strip()
                original_task_name = os.path.join(todo_dir, task_to_rename)
                new_task_name = os.path.join(todo_dir, new_name)
                if os.path.exists(new_task_name):
                    print(f"A task with the name '{new_name}' already exists. Please choose a different name.")
                else:
                    try:
                        os.rename(original_task_name, new_task_name)
                        print(f"Task renamed from '{task_to_rename}' to '{new_name}'")
                    except OSError as E:
                        print(f"An error occurred while renaming the task: {E}")
            else:
                print(f"There is no task with the name '{task_to_rename}'.")
                print("Back...")
                time.sleep(1)
        elif rename_file in ("no", "n", "o"):
            print("Back...")
            time.sleep(1)
        else:
            print("Please check your answer and try again.")
        # Viewing tasks
        print("Tasks to view")
        for i, file in enumerate(get_files_list(), start=1):
            print(f"[#{i}] => {file}")

        # Viewing tasks
        while True:
            v_task = input("Task name to view: ").strip()
            if v_task in files_list:
                try:
                    with open(os.path.join(todo_dir, v_task), "r", encoding="utf-8") as f:
                        print(f.read())
                        break
                except FileNotFoundError:
                    print("")

            elif v_task in ("Exit", "exit", "EXIT"):
                break
            else:
                print(f"There is no task with the name '{v_task}'.")
    else:
        print("Your files list is empty.")


def remove_task():
    files_list = get_files_list()  # Refresh files list
    clear = input("Do you want to clear everything?\n$ ").lower()
    if clear in ("yes", "y"):
        for file in files_list:
            os.remove(fr"{todo_dir}\{file}")
        print("All tasks have been removed successfully.")
    else:
        task_to_remove = input("Tasks that you want to remove [Separated by ',']:\n$ ").strip()
        list_of_tasks_to_remove = task_to_remove.split(",")
        confirmation = input("Do you really want to delete these task files?\n$ ").strip().lower()
        if confirmation in ("yes", "y"):
            for lst in list_of_tasks_to_remove:
                if lst in files_list:
                    try:
                        os.remove(fr"{todo_dir}\{lst}")
                        print(f"{lst} has been removed successfully.")
                    except OSError as E:
                        print(f"Error => {E}")
        else:
            print("Back...")
            time.sleep(1)


# User Interface
while True:
    print("Choose an option: ")
    print("   [1]=> Add")
    print("   [2]=> View")
    print("   [3]=> Delete")
    print("   [4]=> Exit")

    q = input("Option: \n$ ").lower()
    if q == "1" or q == "add":
        add_task()
    elif q == "2" or q == "view":
        view_task()
    elif q == "3" or q == "delete":
        remove_task()
    elif q == "4" or q == "exit":
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please choose a valid option.")

    time.sleep(3)
    print("__"*50)
   