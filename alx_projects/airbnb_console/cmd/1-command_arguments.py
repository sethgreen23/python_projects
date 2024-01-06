#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    # change the prompt
	prompt = ">>>"
	def do_greet(self, person):
		"""greet [person]
		Greet the names person
		"""
		if person:
			print("hi, ", person)
		else:
			print("hi")

	def do_EOF(self, line):
		print("Thank you for using our App.")
		return True

if __name__=="__main__":
    HelloWorld().cmdloop()
