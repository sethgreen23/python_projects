"""
Favorite Fruit
"""
fruits_list = ["banana", "melon", "grape"]
def favorite_fruit(fruit):
    """Check favorite fruit"""
    if fruit in fruits_list:
        print(f"Your realy like {fruit.title()}")
favorite_fruit("banana")
