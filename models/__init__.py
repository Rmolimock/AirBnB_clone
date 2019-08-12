#!/usr/bin/python3
"""Init file sets up FileStorage object and reloads
files from disk
"""

from models.engine.file_storage import FileStorage 

storage = FileStorage()
storage.reload()

