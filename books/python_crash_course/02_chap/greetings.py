from names import names_list

def greeting(name):
	print(f'Hello {name:s}.')

def tell_greeting(n_list):
	for name in n_list:
		greeting(name)
tell_greeting(names_list)
