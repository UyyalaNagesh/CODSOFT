import random


winning_combinations = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


player_score = 0
computer_score = 0

while True:
    
    user_choice = input("Choose rock, paper, or scissors: ")
    user_choice = user_choice.lower()


    computer_choice = random.choice(["rock", "paper", "scissors"])

    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif winning_combinations[user_choice] == computer_choice:
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    
    print("Player score:", player_score)
    print("Computer score:", computer_score)

    
    play_again = input("Do you want to play again? (yes/no): ")
    play_again = play_again.lower()

    if play_again != "yes":
        break