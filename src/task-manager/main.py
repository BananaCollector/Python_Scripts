

def calculate_area(width: float, hight: float) -> float:
    return width * hight


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


def print_tasks(tasks: list[str]) -> None:
    for nr, element in enumerate(tasks):
        print(str(nr+1)+'.', element)


def find_task(tasks: list[str], task: str) -> bool:
    return task in tasks


def count_completed_tasks(tasks: list[dict]) -> int:
    counter = 0
    for task in tasks:
        if task["completed"] is True:
            counter += 1
    return counter


tasks = [
    "Clean dishes",
    "Walk the dog",
    "Buy groceries"
]

tasks_2 = [
    {"title": "Clean dishes", "completed": True},
    {"title": "Walk the dog", "completed": False},
    {"title": "Buy groceries", "completed": True}
]
# ========

print(calculate_area(2, 5))

print(is_even(4), is_even(5), is_even(0))

print(get_full_name('Adam', 'Smith'))

print_tasks(tasks)

print(find_task(tasks, 'Buy groceries'))

print(count_completed_tasks(tasks_2))
