#!/usr/bin/python3
"""This represents the command interpreter console"""


import cmd
from models.__init__ import storage
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
    dot_comms = ["all", "count", "show", "destroy", "update"]

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
            print("** instance id missing **")
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
        all_objects = storage.all()
        if not arg:
            print([str(obj) for obj in all_objects.values()])
            return

        args = arg.split()
        if args[0] not in self.__class_list:
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in all_objects.items() if args[0] in key])

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
        instance.save()

    def precmd(self, line):
        """ Reformat the input """
        __cmd = ""
        __cls = ""
        __id = ""
        __args = ""

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            line_copy = line[:]
            __cls = line_copy[:line_copy.find('.')]
            __cmd = line_copy[line_copy.find('.') + 1:line_copy.find('(')]
            if __cmd not in self.dot_comms:
                print("** command not found **")
            line_copy = line_copy[line_copy.find('(') + 1:line_copy.find(')')]
            if line_copy:
                line_copy = line_copy.partition(', ')
                __id = line_copy[0].replace('\"', '')
                line_copy = line_copy[2].strip()
                if line_copy:
                    if line_copy[2] == '{' and line_copy[-1] == '}' \
                            and type(eval(line_copy)) is dict:
                        __args = line_copy
                    else:
                        __args = line_copy.replace(',', '')
            line = ' '.join([__cmd, __cls, __id, __args])
        except Exception as exc:
            pass
        finally:
            return line

    def do_count(self, args):
        """ Counts the number of instances """
        count = 0
        for key, value in storage.all().items():
            if args == key.split('.')[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
