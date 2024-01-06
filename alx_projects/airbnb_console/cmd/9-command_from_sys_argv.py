#!/usr/bin/env python3
import cmd
import sys

class HelloWorld(cmd.Cmd):
    prompt = ">>> "
    def do_greet(self, line):
        if line:
            print(f"greeting, {line}")
        else:
            print("greeing") 
    def do_hello(self, line):
        print("Hello, it is great to have.")
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
    if len(sys.argv) > 1:
        for line in sys.argv[1:]:
            greeting.onecmd(line)
    else:       
        greeting.cmdloop()
