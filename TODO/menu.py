tasks = []

while True:
  print("Press 1 to add task")
  print("Press 2 to delete task")
  print("Press 3 to view tasks")
  print("Press q to quit")
  choice = input("Enter your choice: ")

  if choice == "1":
    title = input("Enter title of task: ")
    priority = input("Enter priority: High, Medium, Low: ")

    task = {"title": title, "priority": priority}

    tasks.append(task)
    print(tasks)

  elif choice == "2":
    for index in range(0,len(tasks)):
      task = tasks[index]
      print(index + 1, task["title"])

    delete = int(input("Enter number of task to delete: ")) - 1
    del tasks[delete]

  elif choice == "3":
    for index in range(0,len(tasks)):
      task = tasks[index]
      print(index + 1, " - ", task["title"], " - ", task["priority"])

  elif choice == "q":
    break
