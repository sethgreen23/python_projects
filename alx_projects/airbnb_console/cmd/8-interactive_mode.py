#!/usr/bin/env python3
import cmd
import sys

class HelloWorld(cmd.Cmd):
    prompt = ">>> "
    def do_greet(self, line):
        if line:
            print(f"hello, {line}")
        else:
            print("hello")  
    def precmd(self, line):
        # enable cmd depending on the mode
        if sys.stdin.isatty:
            self.prompt = ">>> "
        else:
            self.prompt = ""
        return cmd.Cmd.precmd(self, line)
    def do_EOF(self, line):
        return True
            
if __name__=="__main__":
    greeting = HelloWorld()
    if sys.stdin.isatty():
        #isatty = True
        greeting.cmdloop()
    else:       
        # isatty = False
        for line in sys.stdin:
            greeting.onecmd(line.strip())
