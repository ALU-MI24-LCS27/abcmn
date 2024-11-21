import sys
import os
import time
from datetime import datetime
import signal
import subprocess

"""
Timer sub-command:
    <empty>\t show the timer status
    start\t start the timer
    stop\t stop the timer
    reset\t reset the timer
"""


class BackgroundTimer:
    def __init__(self):
        self.pid_file = os.path.join(".abcmn", "timer.pid")
        self.output_file = os.path.join(".abcmn", "timer_log.lap")
        self.start_time_file = os.path.join(".abcmn", "start_time.lap")

    def write_pid(self, pid):
        with open(self.pid_file, 'w') as f:
            f.write(str(pid))

    def read_pid(self):
        try:
            with open(self.pid_file, 'r') as f:
                return int(f.read().strip())
        except FileNotFoundError:
            return None

    def is_running(self):
        pid = self.read_pid()
        if pid is None:
            return False
        try:
            os.kill(pid, 0)  # Check if process exists
            return True
        except OSError:
            return False

    def start(self, loggable=True):
        if self.is_running():
            if loggable:
                print("Timer is already running!")
            return

        # Store start time
        with open(self.start_time_file, 'w') as f:
            f.write(str(time.time()))

        # Create background process
        process = subprocess.Popen(
            ["bash", "-c", f"""
            while true; do
                curr_time=$(date '+%Y-%m-%d %H:%M:%S')
                start_time=$(cat {self.start_time_file})
                elapsed=$(($(date +%s) - {int(time.time())}))
                hours=$((elapsed / 3600))
                minutes=$(((elapsed % 3600) / 60))
                seconds=$((elapsed % 60))
                printf "[%s] Elapsed time: %02d:%02d:%02d\n" "$curr_time" $hours $minutes $seconds >> {self.output_file}
                sleep 1
            done
            """],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )

        # Store PID
        self.write_pid(process.pid)
        if loggable:
            print(f"Timer started")

    def stop(self, loggable=True):
        pid = self.read_pid()
        if pid is None:
            if loggable:
                print("No timer is running!")
            return

        try:
            # Kill the process group
            os.killpg(os.getpgid(pid), signal.SIGTERM)

            # Calculate total time
            try:
                with open(self.start_time_file, 'r') as f:
                    start_time = float(f.read().strip())
                    elapsed = time.time() - start_time

                with open(self.output_file, 'a') as f:
                    f.write(f"\nTimer stopped at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"Total elapsed time: {elapsed:.2f} seconds\n")
            except FileNotFoundError:
                pass

            # Clean up PID file
            os.remove(self.pid_file)
            os.remove(self.start_time_file)
            if loggable:
                print("Timer stopped")

        except ProcessLookupError:
            print("Timer process not found")
            os.remove(self.pid_file)
        except FileNotFoundError:
            print("PID file not found")

    def reset(self, loggable=True):
        # Stop the timer if it's running
        if self.is_running():
            self.stop(loggable)

        # Clear the log file
        with open(self.output_file, 'w') as f:
            f.write(f"Timer reset at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        if loggable:
            print("Timer reset")

    def status(self, loggable=True):
        if self.is_running():
            try:
                with open(self.start_time_file, 'r') as f:
                    start_time = float(f.read().strip())
                    elapsed = time.time() - start_time
                    hours = int(elapsed // 3600)
                    minutes = int((elapsed % 3600) // 60)
                    seconds = int(elapsed % 60)
                    if loggable:
                        print(f"Timer is running for {hours:02d}:{minutes:02d}:{seconds:02d}")
                    time_stamp = datetime(
                        hour=hours,
                        minute=minutes,
                        second=seconds,
                        year=datetime.now().year,
                        month=datetime.now().month,
                        day=datetime.now().day
                    )
                    return time_stamp.strftime('%H-%M-%S')
            except FileNotFoundError:
                if loggable:
                    print("Timer is running (start time unknown)")
                return None
        else:
            if loggable:
                print("Timer is not running")
            return None


def handle_timer_command(argv):
    __timer_file = os.path.join(".abcmn", "timer_log.lap")
    if not os.path.exists(__timer_file):
        print("No timer log found")
        sys.exit(1)

    timer = BackgroundTimer()
    if len(argv) < 3:
        timer.status()
    elif argv[2] == "start":
        timer.start()
    elif argv[2] == "stop":
        timer.stop()
    elif argv[2] == "reset":
        timer.reset()
    else:
        print("Invalid command for timer")


def __internal_get_timer_status_and_stop():
    __timer_file = os.path.join(".abcmn", "timer_log.lap")
    if not os.path.exists(__timer_file):
        print("No timer log found")
        sys.exit(1)

    timer = BackgroundTimer()
    timer_status = timer.status(loggable=False)
    timer.reset(loggable=False)
    return timer_status if timer_status is not None else "'Timer not running'"
