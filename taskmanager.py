class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename=filename,
        self.tasks = [],
        self.next_id = 1
