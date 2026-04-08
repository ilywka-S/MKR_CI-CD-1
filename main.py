from taskmanager import TaskManager

def run_app():
    # Створюємо екземпляр менеджера
    manager = TaskManager("my_tasks.txt")

    # Демонстрація роботи
    manager.add_task("Вивчити імпорти в Python", prior=1)
    manager.add_task("Написати код для диплому", prior=2)

if __name__ == "__main__":
    run_app()