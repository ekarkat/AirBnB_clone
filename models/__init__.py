#!/usr/bin/python3
#  by sero and mehdi
""" __init__ magic method for models directory."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
