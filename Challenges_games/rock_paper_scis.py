import random

def play_round(computer_choice, user_choice):
    options = ["1. Rock", "2. Paper", "3. Scissors"]
    computer_choice = random.choice(options)
    user_choice = float(input("Please choose (1-3):  "))

    print(f"The computer chose {computer_choice}")

    if user_choice == computer_choice:
        return (f"Both players selected {user_choice}! It's a tie!")
    elif user_choice == "1. Rock":
        if computer_choice == "3. Scissors":
            print("you've won!")
        else: 
            print("you've lost!")
    elif user_choice == "2. Paper":
        if computer_choice == "1. Rock":
            print("you've won!")
        else:
            print("you've lost!")
    elif user_choice == "3. Scissors":
        if computer_choice == "2. Paper":
            print("you've won!")
        else:
            print("you've lost!")
    
    
num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y"

while play_again == "y":
    num_rounds +-1
    result = play_round('computer_choice', 'user_choice')
    if result == "you've won!":
        user_wins += 1
    elif result == "you've lost!":
        computer_wins += 1
else:
    print("It's a tie game!")


print(f"You have played {num_rounds} rounds!")
print(f"You have won {user_wins} game(s)!")
print(f"The computer has won {computer_wins} game(s)!")
play_again = int(input("Would you like to play again?(y/n)  "))
    