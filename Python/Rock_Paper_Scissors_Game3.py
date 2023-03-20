import random

def Data(computer,player):
    print("\nComputer: ",computer)
    print("Player: ",player)

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()

    if player == computer:
        Data(computer=computer,player=player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            Data(computer=computer,player=player)
            print("You lose!")
        else:
            Data(computer=computer,player=player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            Data(computer=computer,player=player)
            print("You lose!")
        else:
            Data(computer=computer,player=player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            Data(computer=computer,player=player)
            print("You lose!")
        else:
            Data(computer=computer,player=player)
            print("You win!")

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")