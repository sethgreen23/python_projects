"""Doc"""


class Monster:
	"""class"""
 

	def __init__(self, health=0, energy=0):
		self.health = health
		self.enery = energy

	#methods
	def attack(self, amount):
		"""Fuck it"""
		print("The moster has attacked")
		print(f"{amount} damage was dealt")
		self.enery -= 30
	def move(self,speed):
		print(f"Monster move {speed} km/h")

monster = Monster(90, 40)
print(monster.health)
monster.attack(20)
print(monster.enery)
monster.move(80)
