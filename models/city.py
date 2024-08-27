#!/usr/bin/python3
"""
Defining the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
