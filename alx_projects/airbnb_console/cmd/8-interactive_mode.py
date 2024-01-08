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
        print("")
        return True
if __name__ == "__main__":
    greeting = HelloWorld()
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
