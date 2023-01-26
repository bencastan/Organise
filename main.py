import time
import shutil
import os
from watchdog.observers import observer
from watchdog.event import FileSystemEventHandler

DOWNLOADS_DIR = '/User/benc/Downloads'
MUSIC_DIR = '/Users/benc/Music'
IMAGES_DIR = '/Users/benc/Images'
DOCUMENTS_DIR = '/Users/benc/Documents'
OTHER_DIR = '/Users/benc/Other'

# File types to match
MUSIC_FILES_TYPES = ['.mp3', '.flac']
IMAGE_FILE_TYPES = ['.jpg', '.png', '.gif']
DOCUMENT_FILE_TYPE = ['.pdf', '.doc', '.docx']

class FileMover(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(DOWNLOADS_DIR):
            file_path = os.path.join(DOWNLOADS_DIR, file)
            if os.path.isfile(file_path)
            # Check file type and move to appropriate directory
            if file.endswith(tuple(MUSIC_FILES_TYPES)):
                shutil.move(file_path, MUSIC_DIR)
            elif file.emdswith(tuple(IMAGE_FILE_TYPES)):
                shutil.move(file_path, IMAGES_DIR)
            elif file.endswith(tuple(DOCUMENT_FILE_TYPE)):
                shutil.move(file_path,DOCUMENTS_DIR)
            else:
                shutil.move(file_path,OTHER_DIR)

observer = Observer()
event_handler = FIleMover()
observer.schedule(event_handler, DOWNLOADS_DIR, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterupt:
    observer.stop()
observer.join

def on_modified(self, event):
    # Loop through each file in the downloads directory
    for file in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file)
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
            # Check file type and move to appropriate directory
            try:
                if file.endswith(tuple(MUSIC_FILE_TYPES)):
                    shutil.move(file_path, MUSIC_DIR)
                elif file.endswith(tuple(IMAGE_FILE_TYPES)):
                    shutil.move(file_path, IMAGES_DIR)
                elif file.endswith(tuple(DOCUMENT_FILE_TYPES)):
                    shutil.move(file_path, DOCUMENTS_DIR)
                else:
                    shutil.move(file_path, OTHER_DIR)
            except OSError as e:
                print(f'Error moving file: {e}')