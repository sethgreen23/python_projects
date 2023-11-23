"""
Chap 5 function
"""
def alien_color(color):
    """Determine Alien colors"""
    if color == "green":
        print("Player earned 5 pointes")
    elif color == "yellow":
        print("Player earned 10 points")
    elif color == "red":
        print("Player earned 15 points")
    else:
        print("Wrong color. Player earn nothing")

alien_color("yellow")
