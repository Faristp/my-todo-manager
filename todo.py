def add_task(task):
    with open("task.txt", "a") as f:
        f.writelines(f"[ ] {task} \n")
    
    print(f"Added task {task}")

def list_task():
    try:
        with open("task.txt", "r") as f:
            
            lines = f.readlines()
            for i, line in enumerate(lines):
                print(f"{i+1}. {line.strip()} ")
    except FileNotFoundError:
        print("No task Yet!")
def mark_done(task):
    try:
        with open("task.txt","r") as f:
            lines = f.readlines()
            found = False
            task_text = " ".join(task)
            if task_text.isdigit():
                i = int(task_text)
                if i > len(lines):
                    print("No task with the id ", i)
                    return
                line = lines[i-1]
                lines[i-1]=lines[i-1].replace("[ ]","[X]")
                with open("task.txt","w") as w:
                    w.writelines(lines)
                    print(f"marked {line[3:].strip()} as done")
                return 
            for i,line in enumerate(lines):
                if task_text in line and "[ ]" in line:
                    lines[i] = line.replace("[ ]","[X]")
                    found = True
                    break
            if not found:
                print("task not found or already Completed")
            else:
                with open("task.txt","w") as f:
                    f.writelines(lines)
        print(f"{task} marked done")
    except FileNotFoundError:
        print("No task to be done!")
import sys
if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1]=="list":
        list_task()
    elif sys.argv[1] == "mark":
        mark_done(sys.argv[2:])
else:
    print("think before you tell") 