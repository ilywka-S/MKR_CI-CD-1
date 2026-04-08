from taskmanager import TaskManager

def run_app():
    manager = TaskManager("my_tasks.txt")

    manager.add_task("Завдання 1", prior=1)
    manager.add_task("Завдання 2", prior=2)
    
    manager.list_tasks(sort_by="priority")

if __name__ == "__main__":
    run_app()