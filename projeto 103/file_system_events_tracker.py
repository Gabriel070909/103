import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/gabri/Downloads/projeto 103"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opa! Alguém excluiu {event.src_path}!")

    def on_modified(self, event):
        print(f"Olá, {event.src_path} foi modificado!")

    def on_deleted(self, event):
        print(f"Alguém moveu {event.src_path} para {event.dest_path}")