#!/usr/bin/python3
"""Module for the console"""

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    Is the main Class for creating the
    command and the action
    """
    prompt = "(hbnb) "
    
    def do_EOF(self, args):
        """EOF method
        """
        return True
    
    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True
    
    def emptyline(self):
        """Empty the last command
        """
        pass
    
    def precmd(self, args):
        """Prepare the command
        """
        if not sys.stdin.isatty():
            print()
        return cmd.Cmd.precmd(self, args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
