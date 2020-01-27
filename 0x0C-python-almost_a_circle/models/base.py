#!/usr/bin/python3

import json


class Base():
    """Class that manage id atributes in all
    child  class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        file = cls.__name__ + ".json"
        json_list = []

        if list_objs:
            for x in list_objs:
                i = x.to_dictionary()
                json_list.append(i)

        json_string = cls.to_json_string(json_list)
        with open(file, mode="w", encoding="utf-8") as new_file:
            new_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string == [] or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            instance = cls(1)
        elif cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as new_file:
                strings_of_instances = new_file.read()
                list_of_dicts = cls.from_json_string(strings_of_instances)
                list_of_instances = []
                for i in list_of_dicts:
                    x = cls.create(**i)
                    list_of_instances.append(x)
                return list_of_instances
        except:
            return []
