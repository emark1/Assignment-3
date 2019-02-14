#To-do List

task_array = []

def show_menu():
    print("""Press 1 to add new task. 
Press 2 to delete task. 
Press 3 to view all tasks.
Press q to quit.""")

user_input = ""

def delete_task():
    for index in range(0,len(task_array)):
        task = task_array[index]
        print(f"""{index + 1} - {task["title"]} - {task["priority"]} priority.""")
    user_input = int(input("Enter number of selection to be deleted: "))
    del task_array[user_input-1]

def view_all_tasks():
    for index in range(0,len(task_array)):
        task = task_array[index]
        print(f"""{index + 1} - {task["title"]} - {task["priority"]} priority.""")
        
def add_new_task():
    task_name = input("Enter name of task: ")
    task_priority = input("Enter priority of task (High, Medium, or Low): ")

    tasks = {"title":task_name, "priority":task_priority}

    task_array.append(tasks)

while user_input != "q":
    show_menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_new_task()
    elif user_input == "3":
        view_all_tasks()
    elif user_input == "2":
        delete_task()
        
