#!/usr/bin/python3
''' This module contains one class, User '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' This class defines a user of the application '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        ''' Initialize a user with BaseModel's atts/methods '''
        super().__init__(self, *args, **kwargs)
