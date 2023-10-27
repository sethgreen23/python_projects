import string
import random

def random_password():
	all_printable = list("".join([string.ascii_letters, string.digits, string.punctuation]))
	# print(all_printable)
	random.shuffle(list(all_printable))
	choice = input("Do you want to create a random password? (Y/N) ")
	while choice.lower() != 'y':
		if (choice.lower() == "n"):
			print("Thank you.See you soon.")
			return
		choice = input("Do you want to create a random password? (Y/N) ")
	pass_length = int(input("Enter the length of the password: "))
	counter = 0
	password = ""
	while counter < pass_length:
		password += random.choice(all_printable)
		counter += 1
	print(f"Your generated password : '{password}'")

random_password()
