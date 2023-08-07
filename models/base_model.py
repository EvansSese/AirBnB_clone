#!/usr/bin/python3
""" This is the Bse Model for the project """


import uuid
from datetime import datetime

class BaseModel:
    """ Defines the base class """
    def __init__(self):
        """ Initializes the base model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Returns the string representation of the model class """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Saves the data """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys / value of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        return (obj_dict)
