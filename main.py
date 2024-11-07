import sys
import os
# import modules
from modules.help_messages import usage_message
from modules.init import init_abcmn_dir
from modules.stats import handle_stats_command
from modules.tasks import handle_tasks_command
from modules.timer import handle_timer_command
from modules.version import __version__ as app_version
from modules.push import handle_push_command

# abcmn cli tool entry point
# read the README.md file for the tool usage information

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc < 2:
        print(usage_message)
        sys.exit(1)

    if argv[1] == "init":
        init_abcmn_dir()
        sys.exit(0)

    if argv[1] == "help":
        print(usage_message)
        sys.exit(0)
    elif argv[1] == "version":
        print(f"Version: {app_version}")
        sys.exit(0)

    __abcmn_dir = os.path.join(".abcmn")
    if not os.path.exists(__abcmn_dir):
        print("Please run 'abcmn init' to initialize the tool")
        sys.exit(1)

    if argv[1] == "push":
        handle_push_command(argv)
    elif argv[1] == "tasks":
        handle_tasks_command(argv)
    elif argv[1] == "timer":
        handle_timer_command(argv)
    elif argv[1] == "stats":
        handle_stats_command()
    else:
        print(usage_message)
        sys.exit(1)
    sys.exit(0)
