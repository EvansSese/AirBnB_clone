#!/usr/bin/python3
"""This is the user information class"""


from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """Represents user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
