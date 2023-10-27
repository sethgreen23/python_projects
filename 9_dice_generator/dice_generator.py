import random

# nee to create dice strings parts
s = "+ - - - - +"
m1 = "|  o   o  |"
m2 = "|    o    |"
m3 = "|  o      |"
m4 = "|      o  |"
m5 = "|         |"
dices = [
	[s, m5, m2, m5, s],
	[s, m3, m5, m4, s],
	[s, m3, m2, m4, s],
	[s, m1, m5, m1, s],
	[s, m1, m2, m1, s],
	[s, m1, m1, m1, s]
]
# generate a dice
def dice(i):
    return dices[i - 1]
#get row by row and join them
def join_rows(*rows):
    return ["	".join(r) for r in zip(*rows)]
# print two dices
def two_dices(a, b, c):
    for line in join_rows(dice(a), dice(b), dice(c)):
        print(line)
# print multiple dices
def ndices(*ns):
    print(ns)
    for line in join_rows(*list(map(dice, ns))):
        print(line)
        
# roll the dice
def roll_dice():
    while (True):
        choice = input("Do you want to roll the dice? (y/n): ")
        while(choice.lower() != 'y'):
            if choice.lower() == 'n':
                print("Thank you for playing. Till next time.")
                return
            choice = input("Do you want to roll the dice? (y/n): ")
        d1 = random.choice(range(1,7))
        d2 = random.choice(range(1,7))
        ndices(d1, d2)
        choice = input("Do you want to exit? (exit): ")
        if choice.lower() == "exit":
            print("Thank you for playing with us. see you next time.")
            return
roll_dice()

# https://stackoverflow.com/questions/52672240/double-dice-graphics-in-python
