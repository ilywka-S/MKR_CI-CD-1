import json

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename=filename,
        self.tasks = [],
        self.next_id = 1

    def load_tasks(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            self.tasks = data

            if self.tasks:
                for id in self.tasks:
                    self.next_id=max(id, self.next_id)+1
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(file)

