import random
import time

def guess_game():
    print("-----Guess Game-----")
    x = int(input("Chose max number: "))
    random_number = int(input("Chose a secret number: "))
    min = 0
    max = x
    while True:
        print(f"Please chose a number between 0 and {x}: ", end="")
        guess = random.randint(min, max)
        time.sleep(1)
        print(f"{guess}")
        time.sleep(1)
        if (guess > random_number):
            print("Sorry, guess again. Too high.")
            max = guess - 1
        elif guess < random_number:
            print("Sorry, guess again. Too low.")
            min = guess + 1
        else:
            print(f"You are a smart computer you guess the number {guess}")
            break
        time.sleep(1)
guess_game()
