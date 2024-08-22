"""
To-Do list for adding and view your entire tasks list
with pryvacy and confident
"""
import subprocess
import os
import datetime
import time
print(datetime.datetime.now())
tasks = []
direction = os.getcwd()
print(direction)
email = "   louhoucode@gmail.com"

def add_task(task):
    """This is just for pylint"""
    tasks.append(task)
    q1 = input("Do you want to write in your new task in a file?\n$ ")
    while True:
        if q1 in ("Yes", "yes", "y", "Y"):
            file_path = fr"{direction}\{task}.txt"
            with open(file_path, "w") as file:
                file.write(task)
            subprocess.run(["notepad.exe", file_path])
            break
        if q1 in ("No", "no", "n", "N"):
            break
    print(f"{task} has been added Successfully.")


while True:
    q = input("add=>[1]/ view=>[2]/ remove[3]: ")
    if q == "1":
        add_task(input("Task name: "))
        time.sleep(2)
