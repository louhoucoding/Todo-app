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
tasks = []
direction = os.getcwd()
# Create Direction of Todo
try:
    os.mkdir(fr"{direction}\Todo_app")
except OSError as e:
    pass
todo_dir = fr"{direction}\Todo_app"
files_list = os.listdir(todo_dir)
if len(files_list) > 0:
    print("Your Todo list =>", ", ".join(file for file in files_list))
else:
    print("Your Todo list => Empty list.")
print(fr"Todo PATH => {direction}\Todo_app")


# Function to add a task.
def add_task(task):
    """
    Func name: Add_task
    :param: task name
    it adds the task to the tasks list
    :return: name of the task added
    """
    if task in files_list:
        print("The task file already exists.")
        q2 = input("Do you want to open it?\n$ ").lower()
        if q2 == "yes":
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

        tasks.append(task)
        print(tasks)

        q1 = input("Do you want to write in your new task file?\n$ ").lower()
        if q1 == "yes":
            with open(new_file, "a", encoding="utf-8") as file:
                file.write(f"# New file named by {task}\n")
            subprocess.Popen(["notepad.exe", new_file])
            pyautogui.hotkey('ctrl', 'end')
            print(f"-{task} has been added Successfully.")
        else:
            print("Back...")


# View the tasks from the list.
def view_task():
    """
    Func name: View_task
    no param
    it view the tasks from the list
    :print: the list of tasks if there is a task list
    """
    if len(files_list) > 0:
        for i, file in enumerate(files_list, start=1):
            print(f"[#{i}] => {file}")
        v_task = input("Task name: ")
        if v_task in files_list:
            with open(fr"{todo_dir}\{v_task}", "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print("There is no task with " + v_task + " name.")
    else:
        print("You files list Is empty.")


def remove_task():
    clear = input("Do you want to clear everything?\n$ ").lower()
    if clear in ("yes", "y"):
        for file in files_list:
            os.remove(fr"{todo_dir}\{file}")
    else:
        ta = " - ".join(files_list)
        if len(files_list) > 0:
            print(ta)
            name_removed_task = input("Task name: ")
            if name_removed_task in files_list:
                q1 = (input(f"Do you really want to delete {name_removed_task}?\n$ ").lower())
                if q1 == "yes":
                    try:
                        os.remove(fr"{todo_dir}\{name_removed_task}")
                        print(f"{name_removed_task} has been deleted.")
                    except OSError as E:
                        print("Error =>", E)
            else:
                print(f"{name_removed_task}, Is not in the list.")

        else:
            print("Your tasks list is empty.")


# Competed task.
def completed_task(num_of_task):
    """
    Func name: Completed_tasks
    :param: num_of_task
    it is for know the Completed_tasks
    :return: Completed tasks
    """
    return num_of_task, "Completed tasks"


# List of Options
print("Choose an option: ")
print("   [1]=> Add")
print("   [2]=> View")
print("   [3]=> Delete")
print("   [4]=> Completed")


# User Interface ==> UI
while True:
    q = (input("Option: \n$ ").lower())
    if q == "1" or q == "add":
        add_task(input("Task name: "))
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


# [1] => Added a function to rename a file I still don't know where
