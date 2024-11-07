import os

config_files = [
    'tasks.json',
    'timer_log.lap',
    'start_time.lap',
    'watcher_log.log',
    'watcher_state.log'
]


# check if the .abcmn directory exists
def init_abcmn_dir():
    if not os.path.exists(".abcmn"):
        os.mkdir(".abcmn")
        for file in config_files:
            with open(os.path.join(".abcmn", file), 'w') as f:
                f.write("")
        # write the empty tasks array
        with open(os.path.join(".abcmn", "tasks.json"), 'w') as f:
            f.write("[]")
        print("Initialized abcmn")
