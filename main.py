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
MUSIC_FILES = ['.mp3', '.flac']
IMAGE_FILE_TYPES = ['.jpg', '.png', '.gif']
DOCUMENTS_DIR = ['.pdf', '.doc', '.docx']

class FileMOver(FileSystemEventHandler):
    