class Monster:
	def __init__(self, health, energy):
		self.health = health
		self.set_energy(energy)

	def update_energy(self, amount):
		self.energy += amount

	def set_energy(self, energy):
		new_enery = energy * 2
		self.energy = new_enery

monster = Monster(health = 100, energy=20)
print(monster.energy)
