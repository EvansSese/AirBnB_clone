#!/usr/bin/python3
""" This is the file storage class """


import os
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dict objects """
        return (self.__objects)

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes obj to JSON file """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes json file to object """
        from models.base_model import BaseModel
        class_map = {"BaseModel": BaseModel,}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, obj_data in obj_dict.items():
                    class_name = obj_data['__class__']
                    if class_name in class_map:
                        class_ = class_map[class_name]
                        obj = class_(**obj_data)
                        self.__objects[key] = obj