import random

while True:
    user_action = input("Enter your choice(rock, paper, scissors ): ")
    possible_actions = ['rock','paper','scissors']
    if user_action in possible_actions:
        computer_action = random.choice(possible_actions)
        print(f"\nYou choose {user_action}, computer choose {computer_action}\n")
    else:
        print(f"\nYour choice {user_action} is not valid\n")
    
    if user_action == computer_action:
        print(f"Both players have selected {user_action}. its a tie!\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors. You win!\n")
        else:
            print("Paper covers rock. You lose!\n")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("Scissors cut paper. You lose!\n")
        else:
            print("Paper covers rock. You win!\n")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("Rock smashes scissors. You lose!\n")
        else:
            print("Scissors cut paper. You win!\n")

    play_again = input("Wanna Play again? (y/n): ")
    if play_again.lower == 'n':
        break

print("\n Goodbyee!")
