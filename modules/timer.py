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

    def start(self):
        if self.is_running():
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
        print(f"Timer started")
        # print(f"Timer started with PID: {process.pid}")
        # print(f"Logging to: {self.output_file}")

    def stop(self):
        pid = self.read_pid()
        if pid is None:
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
            print("Timer stopped")

        except ProcessLookupError:
            print("Timer process not found")
            os.remove(self.pid_file)
        except FileNotFoundError:
            print("PID file not found")

    def reset(self):
        # Stop the timer if it's running
        if self.is_running():
            self.stop()

        # Clear the log file
        with open(self.output_file, 'w') as f:
            f.write(f"Timer reset at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print("Timer reset")

    def status(self):
        if self.is_running():
            try:
                with open(self.start_time_file, 'r') as f:
                    start_time = float(f.read().strip())
                    elapsed = time.time() - start_time
                    hours = int(elapsed // 3600)
                    minutes = int((elapsed % 3600) // 60)
                    seconds = int(elapsed % 60)
                    print(f"Timer is running for {hours:02d}:{minutes:02d}:{seconds:02d}")
            except FileNotFoundError:
                print("Timer is running (start time unknown)")
        else:
            print("Timer is not running")


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