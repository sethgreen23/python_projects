import random

def guess_number(x):
    print("-----Guessing Game-----")
    rand_number = random.randint(1, x)
    #print(rand_number)
    while True:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if (user_guess > rand_number):
            print("Sorry, guess again. Too high.")
        elif user_guess < rand_number:
            print("Sorry, guess again. Too low.")
        else:
            print(f"Very good guess. The secret number is {user_guess}")
            break
guess_number(10)
