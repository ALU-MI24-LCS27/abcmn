import sys
# import modules
from modules.help_messages import usage_message
from modules.tasks import handle_tasks_command
from modules.version import __version__ as app_version

# abcmn cli tool entry point
# read the README.md file for the tool usage information

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc < 2:
        print(usage_message)
        sys.exit(1)
    if argv[1] == "watch":
        print("watch")
    elif argv[1] == "tasks":
        handle_tasks_command(argv)
    elif argv[1] == "timer":
        print("timer")
    elif argv[1] == "stats":
        print("stats")
    elif argv[1] == "version":
        print(f"Version: {app_version}")
    elif argv[1] == "help":
        print(usage_message)
    else:
        print("file path")
    sys.exit(0)
