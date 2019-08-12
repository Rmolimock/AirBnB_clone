#!/usr/bin/python3
import cmd
import sys
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""
module contains 1 class:
    HBNBCommand
"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand is a simple command line
    interpreter for the HBNB project

    Args
        Attributes:
        prompt - Prompt for console
        file - None
        allowed - List of allowed classes
    """
    prompt = "(hbnb) "
    file = None
    
    __allowed = [
        "BaseModel",
        "User",
        "Place",
        "City",
        "Review",
        "State",
        "Amenity"
        ]
    # "User" : User(),
    #             "State" : State(), "City" : City(), "Place" : Place(),
    #             "Amenity" : Amenity(), "Review" : Review()}

    def do_quit(self, arg):
        """quits the program
        """
        self.close()
        return True

    def do_EOF(self, arg):
        """also exits the program
        """
        print()
        self.close()
        return True

    def close(self):
        """closes files before termination
        """
        if self.file:
            self.file.close()
            self.file = None

    def do_create(self, arg):
        """creates a new instance of a model
        and adds it to the json file
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.__allowed:
            print("** class doesn't exist **")
        else:
            args = arg.split()
            obj = eval(str(args[0]) + '()')
            if not isinstance(obj, BaseModel):
                return
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """prints the string representation of a model
        """
        args = arg.split()
        if not args or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__allowed:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        flag = 0
        for key in models.storage.all().keys():
            tmp = str(key).split('.')
            if len(args) > 1 and args[1] in tmp:
                flag = 1
                print(models.storage.objects[(args[0] + "." + args[1])])
        if flag == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance of a model
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__allowed:
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        elif (args[0] + "." + args[1]) not in models.storage.objects.keys():
            print("** no instance found **")
        else:
            del models.storage.objects[args[0] + "." + args[1]]

    def do_all(self, arg):
        """prints all objects of a certain type
        """
        if not arg:
            if models.storage.all().values():
                print([str(obj) for obj in models.storage.all().values()])
        if arg and arg not in self.__allowed:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in models.storage.all().items() if
                   arg in key])

    def do_update(self, arg):
        """updates the value of an attribute for a
        given object
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__allowed:
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")

        obj_id = args[0] + "." + args[1]

        if obj_id not in models.storage.objects.keys():
            print("** no instance found **")
            pass
        elif not args[2]:
            print("** attribute name missing **")
            pass
        elif not args[3]:
            print("** value missing **")
            pass
        else:
            if arg[2] == "updated_at" or arg[2] == "created_at":
                pass
            else:
                setattr(models.storage.objects[obj_id], args[2], args[3])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
