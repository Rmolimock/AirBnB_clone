#!/usr/bin/python3
"""This module contains the State` class for
which inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class for Holberton BnB project
    Args:
        BaseModel: Inherits from BaseModel class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the State obj
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        super().__init__(self, *args, **kwargs)
