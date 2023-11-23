class Hero:
	def __init__(self, damage, monster):
		self.damage = damage
		self.monster = monster
	def attack(self):
		self.monster.get_damage(self.damage)
		return(self.monster.health)

class Monster:
	def __init__(self, health, energy):
		self.health = health
		self.energy = energy
	
	def get_damage(self, damage):
		self.health -= damage

monster = Monster(100, 100)
hero = Hero(30, monster)
hero.attack()
print(monster.health)
