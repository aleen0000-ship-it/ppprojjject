def add_task(tasks, name):
    if name == "":
        print("Invalid task name")
        return tasks
    tasks.append(name)
    return tasks
