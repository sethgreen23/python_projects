def add(a, b):
	return a + b
class Test:
    def __init__(self, add_function):
        self.add_function = add_function
test = Test(add)
print(test.add_function(1,3))

class Monster:
    def __init__(self, func):
        self.func = func
class Attack:

    def bite(self):
        print("bite")

    def strike(self):
        print("strike")

    def slash(self):
        print("strike")

    def kick(self):
        print("kick")
        
attack = Attack()
monster = Monster(attack.bite)
monster.func()
