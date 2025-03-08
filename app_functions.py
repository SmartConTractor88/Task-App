TASK_LIST = "..\\task_app\\task_list.txt"

def read_task_file(filepath=TASK_LIST):
    with open(filepath, "r") as task_file_local: # r for read
        tasks_local = task_file_local.readlines()
    return tasks_local

if __name__ == "__main__":
    read_task_file()

 
def write_task_file(add_tasks, filepath=TASK_LIST): # non-default parameter before the default parameter
    with open(filepath, "w") as task_file: # w for write
        task_file.writelines(add_tasks)

if __name__ == "__main__":
    write_task_file()