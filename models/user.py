#!/usr/bin/python3
"""
Defining the user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class User: first user that inherits
    from BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
