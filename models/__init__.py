#!/usr/bin/python3
''' determine which filestorage method to use based on env variable '''

from models.engine.file_storage import FileStorage 

storage = FileStorage()
storage.reload()

