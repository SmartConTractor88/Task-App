from app_functions import read_task_file, write_task_file # local module
import FreeSimpleGUI as sg
import time
import os # 

sg.theme("LightBrown13")

if not os.path.exists("..\\task_app\\task_list.txt"): # if the task list doesnt exist:
    with open("..\\task_app\\task_list.txt", "w") as file: # create the file if it doesnt exist
        pass # something has to be in this line

##$$ WIDGETS
clock = sg.Text("", key="clock")
label1 = sg.Text("TaskApp") # label on the window
label2 = sg.Text("Enter a task: ")
input_box = sg.InputText(tooltip="Enter a task", key="task") # a simple input





list_box = sg.Listbox(values=read_task_file(), 
                      key="task", enable_events=True,
                      size=[71, 10])

add_button = sg.Button("Add", size=8) # event takes either the label or the key of the widget
edit_button = sg.Button("Edit", size=23)
complete_button = sg.Button("Complete", size=23)
exit_button = sg.Button("Exit:(", size=23, key="Exit:(")
buttons = [edit_button, complete_button, exit_button]
##$$

#layout = [] # the layout can be created as a variable beforehand

window = sg.Window("TaskApp", 
                   layout=[[clock],[label1], [label2, input_box, add_button],
                           [list_box], [buttons]], 
                   font=("Arial", 16))
"""
layout expects a list inside of a list. Inside of the layout argument
we can add everything in one list, which returns all in one line,
or separate lists, which would generate content in different rows
"""

while True:
    event, values = window.read(timeout=200) # display the window and other objects 
    # timeout executes the while loop every 200 miliseconds
    # print(event, values)
    window["clock"].update(value=time.strftime("%d-%b-%Y %H:%M:%S"))

    match event:
        case "Add":
            tasks = read_task_file()
            new_task = values["task"].capitalize() + "\n"
            tasks.append(new_task)
            write_task_file(tasks) # write the new task in the file
            window["task0"].update(values=tasks)

            window["task"].update(value="") # clear the input box when action is done

        case "Edit":
                
            try:    

                task = values["task0"][0]
                new_task = values["task"].capitalize() + "\n"

                tasks = read_task_file()
                index = tasks.index(task)
                tasks[index] = new_task
                write_task_file(tasks)
                window["task0"].update(values=tasks) # update the window with the inserted values

                window["task"].update(value="") # clear the input box when action is done

            except IndexError:
                sg.popup("Please select a task you want to edit.", font="10")

        case "task0":

            window["task"].update(value=values["task0"][0]) # update current selection and place it in the input box

        case "Complete":
                
            try:    

                task = values["task0"][0]

                tasks = read_task_file()
                tasks.remove(task)
                write_task_file(tasks)
                window["task0"].update(values=tasks) # update the window with the inserted values

                window["task"].update(value="")

            except IndexError:
                sg.popup("Please select a task you want to complete.", font="10")

        case "Exit:(":
            break

        case sg.WIN_CLOSED:
            break

window.close()