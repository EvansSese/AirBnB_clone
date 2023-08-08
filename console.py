#!/usr/bin/python3
"""This represents the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Represents command interpreter for HBNB"""

    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
