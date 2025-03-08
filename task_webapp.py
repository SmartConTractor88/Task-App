import streamlit as st 
from app_functions import read_task_file, write_task_file # local module

tasks = read_task_file()

def new_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    write_task_file(tasks)




st.title("TaskApp")

st.subheader("My tasks:")
# st.write("DO MORE! PUSH")

# ADD
for index, task in enumerate(tasks):
    checkbox = st.checkbox(task.capitalize(), key=task)
    if checkbox: # COMPLETE
        tasks.pop(index)
        write_task_file(tasks) # write the new task in the file
        del st.session_state[task]
        st.rerun()

user_input = st.text_input("", placeholder="Write the task here", 
                           on_change=new_task, key="new_task")
