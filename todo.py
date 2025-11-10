def add_task(task):
    with open("task.txt", "a") as f:
        f.write(f"[ ] {task} \n")
    
    print(f"Added task {task}")

def list_task():
    try:
        with open("task.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No task Yet!")

import sys
if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        add_task("".join(sys.argv[2:]))
    elif sys.argv[1]=="list":
        list_task()
        