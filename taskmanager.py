import json
from datetime import datetime
from task import Task

class TaskManager:

    def __init__(self, filename="tasks.txt"):
        self.filename=filename
        self.tasks = []
        self.next_id = 1

    def load_tasks(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            self.tasks = [Task.unwind_dictionary(t) for t in data]

            if self.tasks:
                for id in self.tasks:
                    self.next_id=max(id, self.next_id)+1
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.create_dictionary() for task in self.tasks], file)


    def add_task(self, desc, prior, date = None):
        if not date:
            date = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        task = Task(self.next_id, desc, date, prior)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Завдання додано! ID: {task.task_id}")

    def del_task(self, task_id):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        if len(self.tasks) < initial_count:
            self._save_tasks()
            print(f"Завдання з ID {task_id} видалено.")
        else:
            print(f"Завдання з ID {task_id} не знайдено.")