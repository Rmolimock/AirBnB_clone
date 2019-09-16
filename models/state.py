#!/usr/bin/python3
''' This module contains one class, State '''
from models.base_model import BaseModel


class State(BaseModel):
    ''' This class defines state objects '''
    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialize a state with BaseModel's atts/methods '''
        super().__init__(self, *args, **kwargs)
