# Create a To-do list with python.
"""
datetime module to print the time of starting
using now() function from datetime
"""
import datetime
import os
import subprocess
import time
import pyautogui
print(datetime.datetime.now())
print(datetime.datetime.today())
# List of tasks for the user
direction = os.getcwd()
# Create Direction of Todo
try:
    os.mkdir(fr"{direction}\Todo_app")
except OSError as e:
    pass
todo_dir = fr"{direction}\Todo_app"
print(todo_dir)
files_list = os.listdir(todo_dir)
if len(files_list) > 0:
    print("Your Todo list =>", ", ".join(file for file in files_list))
else:
    print("Your Todo list => Empty list.")
print(fr"Todo PATH => {direction}\Todo_app")


# Function to add a task.
def add_task():
    """
    Func name: Add_task
    :param: task name
    it adds the task to the tasks list
    :return: name of the task added
    """
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
            with open(new_file, "a", encoding="utf-8") as file:
                file.write(f"# New file named by {task}\n")
            subprocess.Popen(["notepad.exe", new_file])
            pyautogui.hotkey('ctrl', 'end')
            print(f"-{task} has been added Successfully.")
        else:
            print("Back...")


def view_task():
    """
    Func name: View_task
    no param
    it view the tasks from the list
    :print: the list of tasks if there is a task list
    """
    if len(files_list) > 0:
        # Display the list of tasks
        for i, file in enumerate(files_list, start=1):
            print(f"[#{i}] => {file}")

        # Asking the user if they want to rename a file
        rename_file = input("Do you want to rename a file? (yes/y or no/n): \n$ ").strip().lower()
        if rename_file in ("yes", "y"):
            task_to_rename = input("Old task name: ").strip()

            # Check if the file exists in the list
            if task_to_rename in files_list:
                new_name = input("Task new name: ").strip()

                # Create the full path for old and new task names
                original_task_name = os.path.join(todo_dir, task_to_rename)
                new_task_name = os.path.join(todo_dir, new_name)
                try:
                    # Renaming the file
                    os.rename(original_task_name, new_task_name)
                    print(f"Task renamed from '{task_to_rename}' to '{new_name}'")
                except FileExistsError:
                    print(f"A task with the name '{new_name}' already exists. Please choose a different name.")
                except OSError as E:
                    print(f"An error occurred while renaming the task: {E}")
            else:
                print(f"There is no task with the name '{task_to_rename}'.")
        elif rename_file in ("no", "n"):
            print("Back...")
        else:
            print("Please check your answer and try again.")

        # Asking the user to view a specific task
        v_task = input("Task name to view: ").strip()
        if v_task in files_list:
            with open(os.path.join(todo_dir, v_task), "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"There is no task with the name '{v_task}'.")
    else:
        print("Your files list is empty.")


# (The split with ',')
def remove_task():
    clear = input("Do you want to clear everything?\n$ ").lower()
    if clear in ("yes", "y"):
        for file in files_list:
            os.remove(fr"{todo_dir}\{file}")
    else:
        task_to_remove = input("Tasks that you want to remove [Separated by ',']:\n$ ").strip()
        list_of_tasks_to_remove = task_to_remove.split(",")
        confirmation = input("Do you really want to delete this tasks file?\n$ ").strip().lower()
        if confirmation in ("yes", "y"):
            for lst in list_of_tasks_to_remove:
                if lst in files_list:
                    try:
                        os.remove(fr"{todo_dir}\{lst}")
                    except OSError as E:
                        print("Error =>", E)
        else:
            print("Back...")
            time.sleep(1)


# Competed task.
def completed_task(num_of_task):
    """
    Func name: Completed_tasks
    :param: num_of_task
    it is for know the Completed_tasks
    :return: Completed tasks
    """
    return num_of_task, "Completed tasks"


# User Interface ==> UI
while True:
    # List of Options
    print("Choose an option: ")
    print("   [1]=> Add")
    print("   [2]=> View")
    print("   [3]=> Delete")
    print("   [4]=> Completed")
    q = (input("Option: \n$ ").lower())
    if q == "1" or q == "add":
        add_task()
        break

    if q == "2" or q == "view":
        view_task()
        break

    if q == "3" or q == "delete":
        remove_task()
        break

    if q == "4" or q == "rename":
        rename_task()

    print("nothing here")

# Admin Interface
