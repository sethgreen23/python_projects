
def add(x, y):
	"""Add Function"""
	return x + y

def sub(x, y):
	"""Subtract Fuction"""
	return x - y

def mul(x, y):
	"""Multiply Function"""
	return x * y

def div(x, y):
	"""Divide Function"""
	if y == 0:
		raise ZeroDivisionError("you can't devide by zero")
	return x // y
