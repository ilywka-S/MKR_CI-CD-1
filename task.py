class Task:
    def __init__(self, task_id, description, date, priority):
        self.task_id = task_id,
        self.description = description,
        self.date = date,
        self.prority = priority

    def create_dictionary(self):
        return {
            "id": self.task_id,
            "desc": self.description,
            "date": self.date,
            "prior": self.prority
        }