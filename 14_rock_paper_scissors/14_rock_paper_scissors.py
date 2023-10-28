import random

def rock_paper_scissors():
    print("-----Rock Paper Scissors-----\n")
    game_choices = ['rock', 'paper', 'scissors']
    while True:
        player1 = random.choice(game_choices).lower()
        player2 = random.choice(game_choices).lower()
        print(f"Player1 Choice: {player1.capitalize()}\nPlayer2 Choice: {player2.capitalize()}")

        if player1 == 'rock':
            if player2 == 'scissors':
                print("Player1 win.")
            elif player2 == 'paper':
                print("Player2 win.")
        elif player1 == 'paper':
            if player2 == 'rock':
                print("Player1 win")
            elif player2 == 'scissors':
                print("Player2 win")
        else:
            if player2 == 'paper':
                print("Player1 win")
            elif player2 == 'rock':
                print("Player2 win")
        if player1 == player2:
            print("It is a Tie.\n")
        print()
        user_input = input("Do you want to play again? (y/n): ").lower()
        while not user_input in 'yn':
            user_input = input("Please chose (y/n): ").lower()
        print()
        if (user_input == 'n'):
            print("Thank you for playing with us.Till next Time.\n")
            break
rock_paper_scissors()
