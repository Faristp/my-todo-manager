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
def mark_done(task):
    try:
        with open("task.txt","r") as f:
            para = f.read().split('\n')    
            for i,p in enumerate(para):
                if task[0] in p:
                    print("task found")
                    para[i]="[Done] "+task[0]
        with open("task.txt","w") as f:
            for i in range(len(para)-1):
                f.write(f"{para[i]} \n")
            f.write(f"{para[-1]}")
        print(f"{task} marked done")
    except FileNotFoundError:
        print("No task to be done!")
import sys
if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        add_task("".join(sys.argv[2:]))
    elif sys.argv[1]=="list":
        list_task()
    elif sys.argv[1] == "mark":
        mark_done(sys.argv[2:])
        