#!/usr/bin/env python3
import cmd
import sys

class HelloWorld(cmd.Cmd):
    prompt = "(hbnb) "
    def do_greet(self, line):
        """Document Greet"""
        if line:
            print(f"hello, {line}")
        else:
            print("hello")
    def onecmd(self, line):
        """onecmd"""
        if not sys.stdin.isatty():
            print("(hbnb)")
        return cmd.Cmd.onecmd(self, line)
    def do_EOF(self, line):
        """Document EOF"""
        print("")
        return True
    
    def do_quit(self, line):
        """Document quit"""
        print("")
        return True

def loop_throw(obj, arg):
    """Loop throw arguments"""
    for line in arg:
        obj.oncmd(line.strip())

if __name__ == "__main__":
    greeting = HelloWorld()
    try:
        if sys.stdin.isatty():
            # isattay = True
            if sys.argv and len(sys.argv) > 1:
                loop_throw(greeting, sys.argv[1:])
            else:
                greeting.cmdloop()
        else:
            # isattay = False
            loop_throw(greeting, sys.stdin)
    except KeyboardInterrupt:
        print("")
