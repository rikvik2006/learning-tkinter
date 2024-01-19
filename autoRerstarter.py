import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd
        self.process = subprocess.Popen(self.cmd)

    def on_modified(self, event):
        if "__pycache__" in event.src_path:
            return
        print(f'File {event.src_path} has been modified, restarting the program.')
        self.process.kill()
        self.process = subprocess.Popen(self.cmd)

if __name__ == "__main__":
    cmd = ['python312', 'main.py']
    event_handler = FileChangeHandler(cmd)
    observer = Observer()
    observer.schedule(event_handler, path='Z:\\4E INFO\\Informatica\\TkInter-github-repo\\tkinter-calculator', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()