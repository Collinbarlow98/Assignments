tasks = []

while True:
    print("Press 1 to add task")
    print("Press 2 to delete task")
    print("Press 3 to view tasks")
    print("Press q to quit")
    choice = input("Enter your choice: ")
    if choice == "q":
        break
    elif choice == "1":
      title = input("Enter title of task: ")
      priority = input("Enter priority; High, Medium, Low: ")
      task = {
        "title": title,
        "priority": priority
      }
      tasks.append(task)
    elif choice == "2":
      for index in range(0,len(tasks)):
        print(index + 1, title)
      delete = int(input("Enter number of task to delete: ")) - 1
      del tasks[delete]
    elif choice == "3":
      for index in range(0,len(tasks)):
        print(index + 1, " - ", title, " - ", priority)
