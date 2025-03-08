### VARIABLES
q1: str = "Add/View/Edit/Complete/Exit: " # upfront question
q2: str = "What is the task?: " # follows the ADD command
q3: str = "Which item would you like to replace?: "
q4: str = "What do you want to replace it with?: "
ans1: str = "Task added."
ans2: str = "You have nothing to do you lazy fuck."

### DEFINITIONS
import time # standard module
from app_functions import read_task_file, write_task_file # local module

#task_file = open("task_list.txt", "w") # w for write, r for read

while True:
    print(time.strftime("%d-%b-%Y %H:%M:%S"))
    user_action: str = input(q1).upper() # program takes the input and converts it into upper case
    user_action: str = user_action.strip() # remove accidental spaces and other stuff
    #match user_action: # old code

    if user_action.startswith("ADD"): # also works for aDd, adD, etc.

        # task = input(q2) # old code
        task: str = user_action[4::] # skip over "add", execute code on the remainder
        task: str = task.capitalize() + "\n" # capitalize the input before continuing

        tasks: list[str] = read_task_file()

        tasks.append(task) # add the input to the list

        write_task_file(tasks, "task_list.txt") # filepath unnecessary
        
        print(ans1) # approval

    elif user_action.startswith("VIEW"):

        tasks: list[str] = read_task_file()

        if len(tasks) == 0: #check if the list got longer
            print(ans2)
        else: # if there is anything on the list...
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
            print("! YOUR TO-DO LIST !")
            for index, task in enumerate(tasks): # add a number to each of the tasks
                print(f"{index+1}. {task.strip()}") # print(f"{index+1}. {task.strip()}")
            print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

    elif user_action.startswith("EDIT"):
            
        try:
        
            print("TASK EDITOR")

            read_task_file()

            if len(tasks) == 0: #check if the list got longer
                print(ans2)
            else: # if there is anything on the list...
                
                write_task_file(tasks, "task_list.txt")

                #item_index = input(q3) # old code
                item_index: int = user_action[5::] # skip over "edit", then read the string

                item_index: int = int(item_index)-1
                tasks[item_index]: str = input(q4).capitalize()
                #del(tasks[item_index]) # delete the corresponding task

                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
                print("! UPDATED TO-DO LIST !")
                for index, task in enumerate(tasks): # add a number to each of the tasks
                    print(f"{index+1}. {task.strip()}") # print(f"{index+1}. {task.strip()}")
                print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

            
        except ValueError:
            print("Invalid command. Type the number of the task you want to edit.")
            continue # run another while loop cycle

    elif user_action.startswith("COMPLETE"):

        try:

            tasks: list[str] = read_task_file()

            completed: int = int(user_action[9::]) # skip over "completed", then read the string
            completed: int = completed-1

            removed_task: str = tasks.pop(completed)
            print(f"Task '{removed_task.strip()}' completed.")

            write_task_file(tasks, "task_list.txt") # update the text file with the previous changes

        except IndexError:
            print("Invalid index. Check the length of the list.")
            continue # run another while loop cycle

    elif "EXIT" in user_action:

        break

    else: # underscore is commonly used in programming
        print("Invalid command.") # will return to the beginning of the while loop

print("Break")