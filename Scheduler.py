def print_to_do_list(to_do_list):
    for index, task in enumerate(to_do_list):
        if task["completed"] == "not completed":
            print(f"{index}. {task["Name"]} at {task["scheduled time"]} is {task["completed"]}")
        else: 
            print(f"{index}. {task["Name"]} at {task["scheduled time"]} was {task["completed"]} at {task["completed time"]}")
tasks = []
while True:
        choice = input("view (v), Add Tasks (a), Quit (q), completed (c), remove task (r) > ")
        if choice == "v":
            print_to_do_list(tasks)
        elif choice == "a":
            addition = input("Please submit the task to add > ")
            addition_time = input("Please submit the scheduled time > ")
            tasks.append({"Name": addition, "completed": "not completed", "scheduled time": addition_time, "completed time": ""})
            print("updated tasks")
            print_to_do_list(tasks)
        elif choice == "c":
            print_to_do_list(tasks)
            try:
                task_index = int(input("Enter the task to complete > "))
                tasks[task_index]["completed"] = "completed"
                addition_time = input("Please submit the completed time > ")
                tasks[task_index]["completed time"] = addition_time
                print("updated tasks")
                print_to_do_list(tasks)
            except ValueError:
                print("Please enter a valid number!")
            except IndexError:
                print("That number is not on the list!")
        elif choice == "r":
            try:
                print_to_do_list(tasks)
                tasks.pop(int(input("Enter the task to remove > ")))
                print_to_do_list(tasks)
            except ValueError:
                print("Please enter a valid number!")
            except IndexError:
                print("That number is not on the list!")
        elif choice == "q":
            break
        else:
            print("Invalid option")
print("Goodbye")