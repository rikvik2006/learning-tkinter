import time
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd
        self.process = subprocess.Popen(self.cmd)

    def on_modified(self, event):
        if "__pycache__" in event.src_path:
            return
        print(f"File {event.src_path} has been modified, restarting the program.")
        self.process.kill()
        self.process = subprocess.Popen(self.cmd)


if __name__ == "__main__":
    cmd = [sys.executable, "main.py"]
    event_handler = FileChangeHandler(cmd)
    observer = Observer()
    observer.schedule(
        event_handler,
        path=Path.joinpath(
            Path(__file__).parent.absolute(), "applicazione-concessionaria"
        ),
        recursive=True,
    )
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
