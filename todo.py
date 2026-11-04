work = []
try:
    with open("tasks.txt", "r") as f:
        for line in f:
            work.append(line.strip())
except FileNotFoundError:
    pass

choose = ""
while choose != "4":
    print("=== To-Do List ===")
    print("1. Look at the list")
    print("2. Add work")
    print("3. Delete work")
    print("4. Exit")
    choose = input("Choose number: ")

    if choose == "1":
        if len(work) == 0:
            print("No tasks yet.")
        else:
            for i, item in enumerate(work, start=1):
                print(i, item)

    elif choose == "2":
        task = input("Enter a task: ")
        work.append(task)
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
        print("Added:", task)
    
    elif choose == "3":
        try:
            number = int(input("Enter the number to delete: "))
            work.pop(number - 1)
            with open("tasks.txt", "w") as f:
                for item in work:
                    f.write(item + "\n")
            print("Deleted task", number)
        except (ValueError, IndexError):
            print("Invalid number.")

    elif choose == "4":
        print("Goodbye!")
        