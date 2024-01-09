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

if __name__ == "__main__":
    greeting = HelloWorld()
    try:
        if sys.stdin.isatty():
            # isattay = True
            print("im in the intereactive mode")
            if sys.argv and len(sys.argv) > 1:
                print("Im inside of the argv")
                for line in sys.argv[1:]:
                    greeting.onecmd(line.strip())
            else:
                print("im not inside of the argv")
                greeting.cmdloop()
        else:
            # isattay = False
            print("Im in the non interactive mode")
            for line in sys.stdin:
                greeting.onecmd(line.strip())
    except KeyboardInterrupt:
        print("")
