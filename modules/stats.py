#!/usr/bin/python3
import os
import sys
# import modules
from modules.tasks import task_manager


class Stats:
    def _init_(self):
        self.completed_tasks = 0
        self.pending_tasks = 0
        self.commits = 0

    def get_stats(self):
        self.completed_tasks = len([task for task in task_manager.list() if task[1].completed])
        self.pending_tasks = len([task for task in task_manager.list() if not task[1].completed])
        self.commits = 0  # TODO: get commits made


def handle_stats_command():
    __tasks_file = os.path.join(".abcmn", "tasks.json")
    if not os.path.exists(__tasks_file):
        print("No tasks found")
        sys.exit(1)

    stats = Stats()
    stats.get_stats()
    print(f"Completed tasks: {stats.completed_tasks}")
    print(f"Pending tasks: {stats.pending_tasks}")
    print(f"Commits made: {stats.commits}")
