#!/usr/bin/env python3
import cmd
import sys

class HelloWorld(cmd.Cmd):
    prompt = "(hbnb) "
    def do_greet(self, line):
        """Documented Greet"""
        if line:
            print(f"greeting, {line}")
        else:
            print("greeing") 
    def do_hello(self, line):
        """Documented Hello"""
        print("Hello, it is great to have.")
    def precmd(self, line):
        # enable cmd depending on the mode
        if sys.stdin.isatty:
            self.prompt = "(hbnb) "
        else:
            self.prompt = ""
        return cmd.Cmd.precmd(self, line)
    def do_quit(self, line):
        """Documented quit"""
        return True
    def do_EOF(self, line):
        """Documented EOF"""
        print("")
        return True
            
if __name__=="__main__":
    greeting = HelloWorld()
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            greeting.onecmd(line)
    else:     
        greeting.cmdloop()
