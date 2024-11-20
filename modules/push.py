import os
import subprocess
from datetime import datetime


def run_command(command):
    """Run a shell command and return output and status"""
    try:
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr


class GitHelper:
    def __init__(self, default_message=None):
        self.__default_message = default_message

    def push_changes(self):
        """Stage, commit and push changes"""
        # Check if we're in a git repository
        success, output = run_command("git rev-parse --is-inside-work-tree")
        if not success:
            print("Error: Not a git repository")
            return False

        # Get status of changes
        success, status = run_command("git status --porcelain")
        if not status.strip() == "":
            # Stage all changes
            success, output = run_command("git add .")
            if not success:
                print(f"Error staging changes: {output}")
                return False

            # Create commit message if not provided
            message = self.__default_message
            if message is None:
                message = f"Update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

            # Commit changes
            success, output = run_command(f'git commit -m "{message}"')
            if not success:
                print(f"Error committing changes: {output}")
                return False

            # Push changes
            success, output = run_command("git push")
            if not success:
                print(f"Error pushing changes: {output}")
                return False

            print("Successfully pushed changes")
            return True
        else:
            print("No changes to push")
            return True


def handle_push_command(argv):
    """Handle push command"""
    default_message = None
    if "--message" in argv:
        index = argv.index("--message")
        default_message = argv[index + 1]
        with open(os.path.join(os.getcwd(), ".abcmn", "default_message.txt"), "w") as file:
            file.write(default_message)
        argv.pop(index + 1)
        argv.pop(index)
    else:
        default_message_file = os.path.join(os.getcwd(), ".abcmn", "default_message.txt")
        if os.path.exists(default_message_file):
            with open(default_message_file, "r") as file:
                default_message = file.read().strip()

    # Push changes
    git_helper = GitHelper(default_message)
    git_helper.push_changes()
