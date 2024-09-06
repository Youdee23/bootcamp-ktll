#!/usr/bin/python3
"""
A module to be used a command prompt for
the running the entire application
"""
import cmd
from projects.models.__init__ import storage
from projects.models.base_model import BaseModel
from projects.models.engine.file_storage import FileStorage
import sys


class AirBNBCommand(cmd.Cmd):
    """
    The cmd is a Python module for creating a program
    that serve as a command line interpreter.
    """
    intro = "Welcome to the AirBNB command program"
    prompt = "airbnb >>> "

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        exit()
    
    def do_emptyline(self, line):
        pass

    def do_create(self, line):
        """ 
        Creates a new instance of base model and saves it to
        the json file and prints the id
        """
        b = BaseModel()
        b.save()
        print(b.id)

        try:
            sys.argv[1]
        except IndexError:
            print("** class name missing **")

        try:
            sys.argv[1]
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and `id`
        """
        self.__str__()

        try:
            sys.argv[1]
        except IndexError:
            print("** class name missing **")

        try:
            sys.argv[1]
        except NameError:
            print("** class doesn't exist **")

        try:
            sys.argv[2]
        except IndexError:
            print("** instance id missing **")

        try:
            sys.argv[1:3]
        except NameError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and `id` (save the change
        into the JSON file)
        """
        try:
            sys.argv[1]
        except IndexError:
            print("** class name missing **")

        try:
            sys.argv[1]
        except NameError:
            print("** class doesn't exist **")

        try:
            sys.argv[2]
        except IndexError:
            print("** instance id missing **")

        try:
            sys.argv[1:3]
        except NameError:
            print("** no instance found **")

        del self.__class__.__name__.id

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """ 
        str_dict = {}      
        if len(sys.argv) == 2:
            for k, v in self.__objects:
                str_dict[k] = v.__str__()
        elif len(sys.argv) == 3:
            self.__str__()
        else:
            pass
            
    def do_update(self, line):
        """
        Updates an instance based on the class name and `id` by adding or 
        updating attribute 
        """
        if type(sys.argv[4]) is not type(sys.argv[3]):
            (type(sys.argv[3])(sys.argv[4]))
        else:
            pass

        try:
            sys.argv[1]
        except IndexError:
            print("** class name missing **")

        try:
            sys.argv[1]
        except NameError:
            print("** class doesn't exist **")

        try:
            sys.argv[2]
        except IndexError:
            print("** instance id missing **")

        try:
            sys.argv[1:]
        except NameError:
            print("** no instance found **")
   
        try:
            sys.argv[3]
        except IndexError:
            print("** attribute name missing **")

        try:
            sys.argv[4]
        except NameError:
            print("** value missing")

        if len(sys.argv) > 5:
            line == sys.argv[:5]
        else:
            pass


if __name__ == "__main__":
    AirBNBCommand().cmdloop()

