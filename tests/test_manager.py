import pytest
from taskmanager import TaskManager


@pytest.fixture
def temp_manager(tmp_path):
    test_file = tmp_path / "test_tasks.json"
    manager = TaskManager(filename=str(test_file))
    return manager


@pytest.mark.parametrize("desc, prior, date", [
    ("Завдання 45", 1, "2023-10-25 10:00"),
    ("Завдання 452", 3, "2023-10-26 12:30"),
    ("Відпочити", 5, "2023-10-27 20:00"),
    ("Завдання без дати", 2, None)
])
def test_add_task(temp_manager, desc, prior, date):
    temp_manager.add_task(desc, prior, date)

    assert len(temp_manager.tasks) == 1

    added_task = temp_manager.tasks[0]
    assert added_task.description == desc
    assert added_task.priority == prior
    assert added_task.task_id == 1

    if date is None:
        assert added_task.date is not None
    else:
        assert added_task.date == date


def test_del_task(temp_manager):
    """Тестуємо видалення завдання за ID."""
    temp_manager.add_task("Завдання 1", 1)
    temp_manager.add_task("Завдання 2", 2)
    assert len(temp_manager.tasks) == 2

    temp_manager.del_task(1)

    assert len(temp_manager.tasks) == 1
    assert temp_manager.tasks[0].task_id == 2
    assert temp_manager.tasks[0].description == "Завдання 2"
