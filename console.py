#!/usr/bin/python3
"""
program to console.py
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class console
    """
    prompt = "(hbnb) "

    def do_EOF(self, *args):
        """Command to exit the program
        """
        return True

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return True
    
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the json file) 
        and prints the id
        """
        lista = args.split(" ")

        if lista[0] == "BaseModel" :
            obj = BaseModel()
            print("{}".format(obj.id))
        elif lista[0] != "BaseModel":
            print("** class doesn´t exist **")
        else:
            print("** class name missing **")
        
    def do_show(self, args):
        """print the string representation of an instance 
        based on the class name and id
        """
        lista = args.split(" ")
        res = BaseModel.__str__.__class__.__name__
        print(res)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
