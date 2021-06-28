#!/usr/bin/python3
"""
program to console.py
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()