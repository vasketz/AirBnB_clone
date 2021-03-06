#!/usr/bin/python3
"""
program to console.py
"""
import cmd
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class_selection = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }


class HBNBCommand(cmd.Cmd):
    """
    class console
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """This is a empty line
        """
        pass

    def do_EOF(self, args):
        """Command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the json file)
        and prints the id
        """
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] in class_selection.keys():
            obj = class_selection[arg[0]]()
            obj.save()
            print("{}".format(obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """print the string representation of an instance
        based on the class name and id
        """
        arg = args.split()
        res = storage.all()
        if arg[0] is "":
            print("** class name missing **")
        elif arg[0] not in class_selection.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in res:
                print("** no instance found **")
            else:
                for keys, value in res.items():
                    if keys == key:
                        print(value)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        arg = args.split()
        res = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in class_selection.keys():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in res:
                del res[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        res = storage.all()
        arg = args.split()
        if len(arg) == 0:
            for keys, value in res.items():
                arg.append(value.__str__())
            print(arg)
        elif arg[0] not in class_selection.keys():
            print("** class doesn't exist **")
        else:
            for keys, value in res.items():
                arg.append(value.__str__())
            print(arg)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        arg = args.split(" ")
        res = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return 0
        elif arg[0] not in class_selection.keys():
            print("** class doesn't exist **")
            return 0
        elif len(arg) == 1:
            print("** instance id missing **")
            return 0
        elif len(arg) == 2:
            print("** attribute name missing **")
            return 0
        elif len(arg) == 3:
            print("** value missing **")
            return 0
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in res.keys():
                res[key].__dict__[arg[2]] = arg[3]
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
