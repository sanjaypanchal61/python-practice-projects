def todo_app():
    tasks = []
    print("-----WELCOME TO THE TASK MANAGEMENT APP-----")

    total_task = int(input("enter how many task you want to add: "))
    for i in range(1, total_task+1):
        task_name = input(f"enter task{i}: ")
        tasks.append(task_name)

    print(f"-----Today's tasks are-----\n{tasks}")

    while True:
        operation = int(input("enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        if operation == 1:
            add = input("enter task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            update_val = input("enter the task name you want to update: ")
            if update_val in tasks:
                up = input("enter new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Updated task {up}")

        elif operation == 3:
            del_val = input("which task you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("close the program")
            break

        else:
            print("Invalid input")

todo_app()
