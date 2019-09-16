#!/usr/bin/python3
"""This module contains the User class for
which inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for Holberton BnB project
    Args:
        BaseModel: Inherits from BaseModel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the User obj
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        super().__init__(self, *args, **kwargs)
