#!/usr/bin/python3
""" Serialization to JSON
Deserialization to JSON """

import json
from models.base_model import BaseModel


class FileStorage():
    """Class that serializes & deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the BaseModel instance"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(self.__file_path, "w", encoding='utf-8') as file:
            (json.dump({k: v.to_dict()
             for k, v in self.__objects.items()}, file))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                self.__objects = ({k: BaseModel(**v)
                                  for k, v in json.load(file).items()})
        except Exception:
            pass
