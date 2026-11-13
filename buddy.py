def add_task(tasks, name):
    """Add a non-empty task name to the task list."""
    if name.strip() == "":
        print("Invalid task name")
        return tasks
    tasks.append(name)
    return tasks
