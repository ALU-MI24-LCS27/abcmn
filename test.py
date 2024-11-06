import sys
from os import system

# import modules
from modules.help_messages import usage_message

# abcmn cli tool entry
"""
Usage: abcmn <command> [options]
Commands:
    watch <path>\t watch a file or directory for changes
    tasks <sub-command>\t manage the tasks
    timer <sub-command>\t manage the timer
    stats\t show the statistics

Tasks sub-command:
    list\t list all tasks
    add\t add a new task
    remove\t remove a task
    update\t update a task
    complete\t mark a task as completed
    uncomplete\t mark a task as uncompleted

Timer sub-command:
    <empty>\t show the timer status
    start\t start the timer
    stop\t stop the timer
    reset\t reset the timer

Options (watch):
    --message\t the commit message template

Variables:
    $file\t the changed file path
    $date\t the current date
"""

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc < 2:
        print(usage_message)
        sys.exit(1)
    if argv[1] == "watch":
        system("python3 main.py watch")
    elif argv[1] == "tasks":
        system("python3 main.py tasks")
    elif argv[1] == "timer":
        system("python3 main.py timer")
    elif argv[1] == "stats":
        system("python3 main.py stats")
    elif argv[1] == "version":
        system("python3 main.py version")
    elif argv[1] == "help":
        print(usage_message)
    else:
        system(f"python3 main.py {argv[1]}")
    sys.exit(0)
