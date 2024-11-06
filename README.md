# abcmn
abcmn is a tool to help with your git workflow, task management, and timing of your coding sessions

## Authors
- Andrew
- Bruce
- Clarisse
- Mutumwinka
- Neema

## Usage
```shell
abcmn <command> [options]
```
### Commands:
- **watch \<path\>**: watch a file or directory for changes and push them to the git repository
- **tasks \<sub-command\>**: manage the tasks
- **timer \<sub-command\>**: manage the timer
- **stats**: show the statistics
- **version**: show the version
- **help**: show the help

### Tasks sub-command:
- **list**: list all tasks
- **add**: add a new task
- **remove**: remove a task
- **update**: update a task
- **complete**: mark a task as completed
- **uncomplete**: mark a task as uncompleted

### Timer sub-command:
- **\<empty\>**: show the timer status
- **start**: start the timer
- **stop**: stop the timer
- **reset**: reset the timer

### Options (watch):
- **--message**: the commit message template

### Variables:
- **\$file**: the changed file path
- **\$date**: the current date