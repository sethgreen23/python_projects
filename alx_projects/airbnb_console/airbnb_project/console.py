#!/usr/bin/python3
"""Module for the console"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Is the main Class for creating the
    command and the action
    """
    prompt = "(hbnb) "
    class_names = ["BaseModel"]
    def do_create(self, args):
        """Create new instance of BaseModel,
			save it and print the id
        """
        # test for the right input
        if not args:
            print("** class name missing **")
            return
        if args not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        #create new instance
        obj = BaseModel()
        # save the new instance
        obj.save()
    
    def do_show(self, args):
        """Print the string representaion of an instance
        based on the class name and i
        """
        #testing the argument
        # test is the name is missing
        # test if the id is missing
        # test if the class name doesnt exist
        # test if the instance of the class name doesnt exist
        # class_exist = False
        class_representation = ""
        go_on = HBNBCommand.validate_args(args)
        if go_on:
            return
        args_list= args.split(" ")
        class_name = args_list[0]
        id = args_list[1]
        for key, kwargs in storage.all().items():
            c_name, c_id = key.split(".")
            if c_id == id and class_name == c_name:
                class_representation = kwargs
                break
        print(class_representation)
    
    def do_destroy(self, args):
        """Delete an instance base on the class name and id
        """
        # test if the class name is missing
        # test if the class name doesnt exist
        # test if id is missing
        # test if the id
        go_on = HBNBCommand.validate_args(args)
        if go_on:
            return
        args_list = args.split(" ")
        class_name = args_list[0]
        id = args_list[1]
        key = f"{class_name}.{id}"
        del storage.all()[key]
        storage.save()
    
    def do_all(self, args):
        """Prints all string representation of all instances based on
        or not the class name
        """
        # test if class doesnt exist
        args_exist = True
        args_list = args.split(" ")
        if args_list[0] != "" and len(args_list) >= 1:
            if args_list[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
                args_exist = False
                return
        obj_list = []
        if args_exist and args_list[0] != "":
            class_name = args_list[0]
            for key, kwargs in storage.all().items():
                c_name, c_id = key.split(".")
                if class_name == c_name:
                    obj_list.append(str(kwargs))
        else:
            for key, kwargs in storage.all().items():
                obj_list.append(str(kwargs))
        print(obj_list)
            
    
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
    
    @staticmethod
    def validate_args(args):
        """Validate arguments
        """
        class_exist = False
        
        if not args:
            print("** class name missing **")
            return 1
        args_list = args.split(" ")
        
        if args_list[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return 1
        
        if len(args_list) < 2:
            print("** instance id missing **")
            return 1
        
        class_name = args_list[0]
        id = args_list[1]
        for key, _ in storage.all().items():
            c_name, c_id = key.split(".")
            if c_id == id and class_name == c_name:
                class_exist = True
                break
        if not class_exist:
            print("** no instance found **")
            return 1
        return 0

if __name__ == '__main__':
    HBNBCommand().cmdloop()
