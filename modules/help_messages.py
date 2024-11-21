usage_message = """Usage: abcmn <command> [options]

Commands:
    init\t initialize the repository
    push\t push changes to the repository
    tasks <sub-command>\t manage the tasks
    timer <sub-command>\t manage the timer
    stats\t show the statistics
    version\t show the version
    help\t show this message

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

Options (push):
    --message\t the commit message template to use once
    --defaultmessage\t the default commit message template when not specified

Variables:
    $date\t the current date
    $timer\t the current timer value
"""
