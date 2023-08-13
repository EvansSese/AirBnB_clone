#!/usr/bin/python3
"""This represents the command interpreter"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Represents command interpreter for HBNB"""

    prompt = '(hbnb) '
    __class_list = ["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exits the command interpreter on EOF"""
        print()
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """ Create new instance and save it """
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Print the string representation of an instance """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return
        instance_id = args[1]
        all_objects = storage.all()
        instance_key = "{}.{}".format(args[0], instance_id)
        if instance_key in all_objects:
            print(all_objects[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance based on class name and id """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        instance_key = "{}.{}".format(args[0], instance_id)
        if instance_key in all_objects:
            del all_objects[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Print string representation of all instances """
        args = arg.split()
        if not args or args[0] in self.__class_list:
            if args:
                class_name = args[0]
                instances = storage.all(class_name)
            else:
                instances = storage.all()

            print([str(obj) for obj in instances.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update instance based on class name and id """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objects = storage.all()
        instance_key = "{}.{}".format(args[0], instance_id)
        if instance_key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instance = all_objects[instance_key]
        setattr(instance, attribute_name, attribute_value)
        instance_save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
