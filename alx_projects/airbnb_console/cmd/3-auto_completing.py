#!/usr/bin/env python3

try:
    import sys
    import gnureadline
    sys.modules["readline"] = gnureadline
except ImportError:
    pass
import cmd

class HelloWorld(cmd.Cmd):
    FRIENDS = ["Alice", "Adam", "Barbara", "Bob"]
    
    def do_greet(self, person):
        "Greet a person"
        if person and person in self.FRIENDS:
            greeting = f'hi, {person}'
        elif person:
            greeting = f'hello, {person}'
        else:
            greeting = "hello"
        print(greeting)
    # customize the autocomplite of the command
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [
				f
				for f in self.FRIENDS
				if f.startswith(text.lower().capitalize())
			]
        return completions
    
    def do_EOF(self, line):
        print("Thank you for using the app.")
        return True

if __name__=="__main__":
    HelloWorld().cmdloop()
            
        
