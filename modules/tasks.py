#!/usr/bin/python3
import json
import os

from modules.help_messages import usage_message


class Task:
    """
    Task class
    """

    # def __init__(self, name, completed=False):
    #     self.__name = name
    #     self.__completed = completed

    # def __str__(self):
    #     return f"{self.__name} {'[x]' if self.__completed else '[ ]'}"

    # def __repr__(self):
    #     return self.__str__()

    # def mark_as_completed(self):
    #     self.__completed = True

    # def mark_as_uncompleted(self):
    #     self.__completed = False

    # def update(self, name):
    #     self.__name = name

    def to_dict(self):
        return {"name": self.__name, "completed": self.__completed}

    @staticmethod
    def from_dict(data):
        return Task(data["name"], data["completed"])

    @property
    def name(self):
        return self.__name

    @property
    def completed(self):
        return self.__completed


class TaskManager:
    """
    Task manager class
    """
    __tasks_file = os.path.join(".abcmn", "tasks.json")

    def __init__(self):
        self.__tasks = []
        self.__current_task = None
        self.load()

    def load(self):
        if os.path.exists(self.__tasks_file):
            with open(self.__tasks_file, "r") as file:
                loaded_json = json.load(file)
                self.__tasks = [Task.from_dict(task) for task in loaded_json["tasks"]]
                self.__current_task = json.load(file).current if loaded_json["current"] is not None else None

    def save(self):
        os.makedirs(os.path.dirname(self.__tasks_file), exist_ok=True)
        with open(self.__tasks_file, "w") as file:
            json.dump({
                "current": self.__current_task,
                "tasks": [task.to_dict() for task in self.__tasks]
            }, file)

    def add(self, task):
        self.__tasks.append(task)
        self.save()

    def remove(self, task):
        self.__tasks.remove(task)
        self.save()

    def update(self, task, name):
        task.update(name)
        self.save()

    def mark_as_completed(self, task):
        task.mark_as_completed()
        self.save()

    def mark_as_uncompleted(self, task):
        task.mark_as_uncompleted()
        self.save()

    def list(self):
        return [(index, task) for index, task in enumerate(self.__tasks)]  # [(index, task)]

    def get_current_task(self) -> Task:
        return self.__tasks[self.__current_task] if self.__current_task is not None else None

    def set_current_task(self, task):
        self.__current_task = self.__tasks.index(task)
        self.save()


task_manager = TaskManager()


def add_task():
    task_name = input("Enter the task name: ")
    task_manager.add(Task(task_name))


def remove_task():
    _tasks = task_manager.list()
    if not _tasks:
        print("No tasks found.")
        return
    for index, task in _tasks:
        print(f"{index + 1}. {task}")
    task_index = int(input("Enter the task index to remove: ")) - 1
    task_manager.remove(_tasks[task_index][1])


def update_task():
    _tasks = task_manager.list()
    if not _tasks:
        print("No tasks found.")
        return
    for index, task in _tasks:
        print(f"{index + 1}. {task}")
    task_index = int(input("Enter the task index to update: ")) - 1
    task_name = input("Enter the new task name: ")
    task_manager.update(_tasks[task_index][1], task_name)


def complete_task(loggable=True):
    _tasks = task_manager.list()
    if not _tasks:
        if loggable:
            print("No tasks found.")
        return "No tasks found"
    for index, task in _tasks:
        print(f"{index + 1}. {task}")
    task_index = int(input("Enter the task index to mark as completed: ")) - 1
    task_manager.mark_as_completed(_tasks[task_index][1])
    return _tasks[task_index][1].name


def uncomplete_task(loggable=True):
    _tasks = task_manager.list()
    if not _tasks:
        if loggable:
            print("No tasks found.")
        return
    for index, task in _tasks:
        print(f"{index + 1}. {task}")
    task_index = int(input("Enter the task index to mark as uncompleted: ")) - 1
    task_manager.mark_as_uncompleted(_tasks[task_index][1])
    return _tasks[task_index][1]


def list_tasks():
    _tasks = task_manager.list()
    if not _tasks:
        print("No tasks found.")
        return
    for index, task in _tasks:
        print(f"{index + 1}. {task}")


def handle_tasks_command(argv):
    if len(argv) < 3:
        print(usage_message)
        return
    sub_command = argv[2]
    if sub_command == "list":
        list_tasks()
    elif sub_command == "add":
        add_task()
        task_manager.save()
        print("Task saved.")
    elif sub_command == "remove":
        remove_task()
        task_manager.save()
        print("Task saved.")
    elif sub_command == "update":
        update_task()
        task_manager.save()
        print("Task saved.")
    elif sub_command == "complete":
        complete_task()
        task_manager.save()
        print("Task saved.")
    elif sub_command == "uncomplete":
        uncomplete_task()
        task_manager.save()
        print("Task saved.")
    else:
        print(usage_message)
        return


def __internal_complete_task():
    return complete_task(loggable=False)
