def add(a, b):
    """
	Function that adds two numbers
    """
    return a + b
def sub(a, b):
    """
    Function that substract two numbers
    """
    return a - b
def mul(a, b):
    """
    Function that multiplier two numbers
    """
    return a * b
def div(a, b):
    """
    Function that divide two numbers
    """
    return a / b
def calculator():
    """
    Simple calculator that provide
    addition
    substruction
    multiplication
    division
    between two numbers
    """
    while (True):
        c = input("Enter the operator: (+, -, *, /, exit): ")
        if (c.lower() == "exit"):
            break
        elif (not c in "+-*/"):
            print("Wrong operator please chose a proper choice: ")
            continue
        
        a = int(input("Enter the first operand: "))
        b = int(input("Enter the second operand: "))
        if c == '+':
            print(f'{a} + {b} = {add(a, b)}')
        elif c == '-':
            print(f'{a} - {b} = {sub(a, b)}')
        elif c == '*':
            print(f'{a} * {b} = {mul(a, b)}')
        elif c == '/':
            print(f'{a} / {b} = {div(a, b)}')
            
    
calculator()
