from taskmanager import TaskManager

def run_app():
    manager = TaskManager("tasks.txt")

    while True:
        print("1. Показати завдання (за пріоритетом)")
        print("2. Показати завдання (за датою)")
        print("3. Додати нове завдання")
        print("4. Видалити завдання")
        print("0. Вийти з програми")

        choice = input("Оберіть дію (0-4): ").strip()

        if choice == "1":
            manager.list_tasks(sort_by="priority")

        elif choice == "2":
            manager.list_tasks(sort_by="date")

        elif choice == "3":
            desc = input("Введіть опис завдання: ").strip()
            if not desc:
                print("Опис не може бути порожнім!")
                continue

            try:
                prior = int(input("Введіть пріоритет (наприклад, 1-5): "))
                manager.add_task(desc, prior=prior)
            except ValueError:
                print("Помилка: Пріоритет має бути цілим числом!")

        elif choice == "4":
            try:
                task_id = int(input("Введіть ID завдання для видалення: "))
                manager.del_task(task_id)
            except ValueError:
                print("Помилка: ID має бути цілим числом!")

        elif choice == "0":
            break

        else:
            print("Невідома команда. Будь ласка, введіть число від 0 до 4.")

if __name__ == "__main__":
    run_app()
