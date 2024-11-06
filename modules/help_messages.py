usage_message = """
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
