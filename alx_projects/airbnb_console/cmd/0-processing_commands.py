#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    prompt = ">>>"
    def do_greet(self, line):
        '''
		Greet the user with a word
        '''
        print(line)
    
    def do_EOF(self, line):
        print("Thank you for using our app.")
        return True


if __name__=="__main__":
    HelloWorld().cmdloop()
