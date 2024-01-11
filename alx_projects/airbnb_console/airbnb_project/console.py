#!/usr/bin/python3
"""Module for the console"""

import cmd
import sys
import importlib
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Is the main Class for creating the command and the action
    """
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                   "Review"]

    def do_create(self, args):
        """Create new instance of BaseModel, save it and print the id
        """
        # test for the right input
        if not args:
            print("** class name missing **")
            return
        if args not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        # create new instance
        obj = args()
        # save the new instance
        obj.save()

    def do_show(self, args):
        """Print the string representaion of an instance based on the class
name and i
        """
        # testing the argument
        # test is the name is missing
        # test if the id is missing
        # test if the class name doesnt exist
        # test if the instance of the class name doesnt exist
        # class_exist = False
        class_representation = ""
        go_on = HBNBCommand.validate_args(args)
        if go_on:
            return
        args_list = args.split(" ")
        class_name = args_list[0]
        id = args_list[1]
        for key, kwargs in storage.all().items():
            c_name, c_id = key.split(".")
            if c_id == id and class_name == c_name:
                class_representation = kwargs
                break
        print(class_representation)

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

    def do_create(self, args):
        """Create new instance of BaseModel,
            save it and print the id
        """
        # test for the right input
        if not args:
            print("** class name missing **")
            return
        class_name = args.split(" ")[0]
        if class_name not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        copy_class_name = class_name
        if copy_class_name == "BaseModel":
            copy_class_name = "Base_Model"
        module_name = f"models.{copy_class_name.lower()}"
        module = importlib.import_module(module_name)
        class_obj = getattr(module, class_name)

        # create new instance
        obj = class_obj()
        # save the new instance
        obj.save()

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
updating attribute"""
        # check if class name is missing
        # check if class name is a valid class name. eg. BaseModel
        # check if id is missing
        # check if an insntance of the class with the id provided exisits
        # check if attribute name is missing
        # check if the attribute value exists
        self.cmdName = "update"
        go_on = HBNBCommand.validate_args(args, self.cmdName)
        if go_on:
            return

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
        # We need to check if the console is interacting with a terminal in the
        # preloop() method
        if not sys.stdin.isatty():
            print()
        return cmd.Cmd.precmd(self, args)

    def onecmd(self, line):
        """Onecmd implementation"""
        args_list = line.split(".")

        if len(args_list) > 1:
            class_name = args_list[0]
            command = args_list[1].strip("()")
            line = f"{command} {class_name}"

        return cmd.Cmd.onecmd(self, line)

    def do_count(self, line):
        """Do counting of instances"""
        # check if class name exists
        # if it does not exist, print '0' and return
        # initialize counter
        # loop through storage.all()
        # extract the class_name
        # compare the class_name with the argument from onecmd
        #       if class_name found:
        #       increment counter
        # print(count)
        count = 0
        args_list = line.split()
        class_name = args_list[0]
        if class_name not in HBNBCommand.class_names:
            print(count)
            return
        for key, kwargs in storage.all().items():
            c_name, _ = key.split(".")
            if class_name == c_name:
                count += 1
        print(count)

    # def preloop(self):
    #     """checks if console is interacting with a terminal or not
    #     """
    #     if not sys.stdin.isatty():
    #         print()

    @staticmethod
    def validate_args(args, cmdName=None):
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
        if cmdName == "update":
            return (HBNBCommand.validate_update(args_list, class_name))
        return 0

    @staticmethod
    def validate_update(args_list, class_name):
        """Helper function for validate args in the case of update cmd"""
        if len(args_list) >= 3:
            if len(args_list) >= 4:
                # add attribute or update its value if it exists
                if type(args_list[3]) not in [str, int, float]:
                    return
                else:
                    attr_name = args_list[2]
                    attr_value = args_list[3].strip("\"")
                    # use ID to search for instance
                    # for key, value in storage.all().items():
                    search_key = f"{args_list[0]}.{args_list[1]}"

                    for key, value in storage.all().items():
                        if key == search_key:
                            if hasattr(storage.all()[key], attr_name):
                                attr_type = type(getattr(storage.all()[key],
                                                         attr_name)).__name__
                                if attr_type == "int":
                                    setattr(storage.all()[key], attr_name,
                                            int(attr_value))
                                elif attr_type == "str":
                                    setattr(storage.all()[key], attr_name,
                                            str(attr_value))
                                elif attr_type == "float":
                                    setattr(storage.all()[key], attr_name,
                                            float(attr_value))
                            else:
                                setattr(storage.all()[key], attr_name,
                                        str(attr_value))
                    storage.save()

                    # class_name.attr_name = attr_value
                    pass
            else:
                print("** value missing **")
                return 1
        else:
            print("** attribute name missing **")
            return 1
        return 0


if __name__ == '__main__':
    HBNBCommand().cmdloop()
