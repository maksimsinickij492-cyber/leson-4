
class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.done = False

    def show(self):
        status = "Виконано" if self.done else "Не виконано"
        print(f"Назва: {self.name}")
        print(f"Опис: {self.description}")
        print(f"Дедлайн: {self.deadline}")
        print(f"Стан: {status}")
        print("-" * 30)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Завдання додано!")

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print("Завдання видалено!")
                return
        print("Завдання не знайдено!")

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.done = True
                print("Завдання виконано!")
                return
        print("Завдання не знайдено!")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній!")
        else:
            for task in self.tasks:
                task.show()


# Створення менеджера
manager = TaskManager()

# Головне меню
while True:
    print("\n=== МЕНЕДЖЕР ЗАВДАНЬ ===")
    print("1. Додати завдання")
    print("2. Видалити завдання")
    print("3. Позначити як виконане")
    print("4. Показати всі завдання")
    print("5. Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Назва завдання: ")
        description = input("Опис: ")
        deadline = input("Дедлайн: ")

        task = Task(name, description, deadline)
        manager.add_task(task)

    elif choice == "2":
        name = input("Назва завдання для видалення: ")
        manager.delete_task(name)

    elif choice == "3":
        name = input("Назва виконаного завдання: ")
        manager.complete_task(name)

    elif choice == "4":
        manager.show_tasks()

    elif choice == "5":
        print("Програму завершено!")
        break

    else:
        print("Неправильний вибір!")
