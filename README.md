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
- **init**: initialize the abcmn tool
- **push**: push changes to the repository
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
- **uncomplete**: mark a task as uncompleted by the user

### Timer sub-command:
- **\<empty\>**: show the timer status
- **start**: start the timer
- **stop**: stop the timer
- **reset**: reset the timer

### Options (push):
- **--message**: the commit message template to use once
- **--defaultmessage**: the default commit message template to use when not specified

### Variables (used in commit message template):
- **{{date}}**: the current date
- **{{timer}}**: the current timer value
- **{{task}}**: the current task
<br/>

<br/>*This project is still in development, so please be patient and stay tuned for updates!*
<br/>*Windows support is coming soon...*
<br/>*Feel free to contribute to the project by forking the repository and submitting a pull request!*
<br/>*In case of any issues, please submit an issue on the repository!*
<br/>*To learn more about how git works watch [Git Internals](https://www.youtube.com/watch?v=fWMKue-WBok&list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7)*<br/>
<br/>*Thank you for your support!*
