#!/usr/bin/env python3
import cmd
import sys

class HelloWorld(cmd.Cmd):
    prompt = ">>>"    
    def do_greet(self, line):
        if line:
            print(f"hello, {line}")
        else:
            print("hello")
    def preloop(self):
        if sys.stdin.isatty():
            self.prompt = ""
        return cmd.Cmd.preloop(self)      
    
    def do_EOF(self, line):
        return True
    
if __name__=="__main__":
    greeting = HelloWorld()
    if sys.stdin.isatty():
        for line in sys.stdin:
            greeting.onecmd(line.strip())
    else:
        greeting.cmdloop()
