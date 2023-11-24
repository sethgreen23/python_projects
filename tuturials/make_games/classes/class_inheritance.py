class Monster:
	def __init__(self, energy, health, **kwargs):
		super().__init__(**kwargs)
		self.energy = energy
		self.health = health
	
	def attack(self, amount):
		print("The Monster attacks")
		self.health -= amount
		print(f"Attack {amount} delt")
	
	def move(self):
		print("Monster moves")
		print(f"{self.health} is Monster health")

class Fish:
	def __init__(self, speed, has_scale, **kwargs):
		super().__init__(**kwargs)
		self.speed = speed
		self.has_scale = has_scale
	def swim(self):
		print(f"The fish swim at a speed of {self.speed}")

class Shark(Monster, Fish):
	def __init__(self, bite_strength, energy, health, speed, has_scale):
		super().__init__(energy=energy, health=health, speed=speed, has_scale=has_scale)
		self.bite_strength = bite_strength
	def bite(self):
		print("Shark bites")
		print(f"Shark bite strength {self.bite_strength}")

shark = Shark(bite_strength=25,
				energy=120,
				health=200,
				speed=180,
				has_scale=False)
#print(Shark.mro())
shark.move()
print(shark.health)
shark.attack(30)
print(shark.health)
shark.bite()
