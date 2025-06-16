import time 
import yaml 
import os
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, app, logger, config_path, on_reload, debounce_seconds):
        super().__init__()
        self.app = app 
        self.logger = logger 
        self.config_path = os.path.abspath(config_path)
        self.on_reload = on_reload
        self.debounce_seconds = debounce_seconds 
        self.last_modified = 0 

    def on_modified(self, event):
        if os.path.abspath(event.src_path) != self.config_path:
            return 
        
        now = time.time() 
        if now - self.last_modified < self.debounce_seconds:
            return
        
        self.last_modified = now 
        if self.logger is not None:
            self.logger.info("YAML file changed. Reloading...")

        self.on_reload(config_file = self.config_path) 

def start_yaml_watcher(app, logger, config_path, on_reload, debounce_seconds):
    event_handler = ChangeHandler(app, logger, config_path, on_reload, debounce_seconds)
    observer = Observer() 
    observer.schedule(event_handler, path=os.path.dirname(os.path.abspath(config_path)), recursive=False) 
    observer.start() 