#!/usr/bin/env python3
import cmd

class HelloWorld(cmd.Cmd):
    
    #disable the rowimput module
    use_rawinput = False
    
    # do not show a prompt after each command read
    prompt = ''
    
    def do_greet(self, line):
        print("hello, ", line)
    
    def do_EOF(self, line):
        return True
    
if __name__=="__main__":
	import sys
	with open(sys.argv[1], 'rt') as input:
		HelloWorld(stdin=input).cmdloop()
