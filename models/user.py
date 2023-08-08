#!/usr/bin/python3
"""This is the user information class"""


from models.base_model import BaseModel
from models import storage
from models.user import User


class User(BaseModel):
    """Represents user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
