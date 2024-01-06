#!/usr/bin/env python3

#Set up gnureadline as readline if installed
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd

class HelloWorld(cmd.Cmd):
    prompt = ">>>"
    def do_greet(self, person):
        if person:
            print("hi, ", person)
        else:
            print("hi")
    # create helper function for greet command
    def help_greet(self):
        print('\n'.join([
            "greet [person]",
            "Gree the named person"
        ]))
    def do_EOF(self, line):
        print("Thank you for using out application")
        return True

if __name__=="__main__":
    HelloWorld().cmdloop()
