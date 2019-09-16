#!/usr/bin/python3
''' This module contains one class, HBNBCommand '''
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    ''' This class creates a command line console for testing '''

    prompt = "(hbnb) "

    __g_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def do_EOF(self, arg):
        ''' exit the console '''
        return True

    def emptyline(self):
        ''' do nothing on empty line '''
        return False

    def do_quit(self, arg):
        ''' quit the console '''
        return True

    def g_classes(self):
        ''' returns private variable much like a getter '''
        return HBNBCommand.__g_classes

    def split_line(self, line):
        ''' split the input line into key/values '''
        data = {}
        for each in line:
            k, v = line.split('=', 1)
            # if the value is a string, replace whitespace
            if v[0] == v[-1] == '"':
                v = shlex.split(v)[0].replace('_', ' ')
            else:
                try:
                    if '.' in k:
                        v = float(v)
                    else:
                        v = int(v)
                except:
                    pass
            data[k] = v
        return data

    def check_class_name(self, args):
        ''' checks if class name was passed and if exists '''
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] not in self.g_classes():
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, line):
        ''' create new instance of obj and save using FileStorage '''
        args = line.split()
        if self.check_class_name(args) is False:
            return False
        name = args[0]
        data = self.split_line(args[1:])
        obj = self.g_classes()[name](**data)
        print(obj.id)
        obj.save()

    def do_show(self, line):
        ''' print info about an instance '''
        args = line.split()
        if self.check_class_name(args) is False:
            return False
        name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return False
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return False
        print(models.storage.all()[key])

    def do_destroy(self, line):
        ''' delete an object from storage '''
        args = line.split()
        if self.check_class_name(args) is False:
            return False
        name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return False
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return False
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, line):
        ''' print list of objects in storage '''
        if not line:
            # prints all objects
            print([str(v) for v in models.storage.all().values()])
        else:
            # if user specifies a class
            objects = []
            args = line.split()
            name = args[0]
            if self.check_class_name(args) is False:
                return False
            for k, v in models.storage.all().items():
                if name in k:
                    objects.append(str(v))
            if len(objects) < 1:
                return False
            print(objects)

    def do_update(self, line):
        ''' update an instance with new attr values '''
        args = line.split()
        if self.check_class_name(args) is False:
            return False
        name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return False
        _id = args[1]
        attr = args[2]
        value = args[3]
        obj = models.storage.all()[name + '.' + _id]
        try:
            if '.' in value:
                value = float(value)
            else:
                value = int(value)
        except:
            pass
        obj.__dict__[attr] = value
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
