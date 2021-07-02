#!/usr/bin/python3
"""
program to console.py
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User


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
        arg = args.split(" ")
        if arg[0] == "":
            print("** class name missing **")
        elif arg[0] == "BaseModel":
            obj = BaseModel()
            obj.save()
            print("{}".format(obj.id))
        elif arg[0] == "User":
            obj = User()
            obj.save()
            print("{}".format(obj.id))
        elif arg[0] != "BaseModel" and arg[0] != "User":
            print("** class doesn't exist **")

    def do_show(self, args):
        """print the string representation of an instance
        based on the class name and id
        """
        arg = args.split(" ")
        res = storage.all()
        if arg[0] is "":
            print("** class name missing **")
        elif arg[0] != "BaseModel" and arg[0] != "User":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "BaseModel.{}".format(arg[1])
            key1 = "User.{}".format(arg[1])
            if key not in res and key1 not in res:
                print("** no instance found **")
            else:
                for keys, value in res.items():
                    if keys == key or keys == key1:
                        print(value)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        arg = args.split(" ")
        res = storage.all()
        if arg[0] is "":
            print("** class name missing **")
        elif arg[0] != "BaseModel" and arg[0] != "User":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "BaseModel.{}".format(arg[1])
            key1 = "User.{}".format(arg[1])
            if key in res:
                del res[key]
            if key1 in res:
                del res[key1]
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        res = storage.all()
        arg = args.split(" ")
        if arg[0] is None:
            for keys, value in res.items():
                arg.append(value.__str__())
            print(arg)
        elif arg[0] != "BaseModel" and arg[0] != "User":
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
        if arg[0] == "":
            print("** class name missing **")
        elif arg[0] != "BaseModel" and arg[0] != "User":
            print("** class doesn't exist **")
        elif len(arg) == 1 and arg[0] != "":
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            key = "BaseModel.{}".format(arg[1])
            key1 = "User.{}".format(arg[1])
            if key in res:
                res[key].__dict__[arg[2]] = arg[3]
                res[key].save()
            if key1 in res:
                res[key1].__dict__[arg[2]] = arg[3]
                res[key1].save()
            else:
                print("** no instance found **")
