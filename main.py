import random 
options = [1,2,3] 
play_again = 1
user_wins = 0
comp_wins = 0
choice = ["rock", "scissors","paper"]

print("Welcome to the rock scissors paper game! Do you know the rules?")
rules_needed = input("Type y/n: ").lower()
if rules_needed == "n":
    print("Rock beats scissors, scissors beats paper, paper beats rock. If you play the same as the computer, its a draw. Good luck!")

def game():
    print()
    global user_wins
    global comp_wins
    global play_again
    print("CHOOSE EITHER ROCK (type 1), SCISSORS (type 2) OR PAPER (type 3)")
    user_choice = int(input())
    comp_choice = random.choice(options)
    print(comp_choice)
    if user_choice - comp_choice == -1 or user_choice - comp_choice == 2:
        print("You win this round!")
        print("You chose", choice[user_choice - 1], "and the computer chose", choice[comp_choice - 1])
        user_wins += 1
    elif user_choice == comp_choice:
        print("Its a draw!")
        print("You chose", choice[user_choice - 1], "and the computer chose", choice[comp_choice - 1])
    else:
        print("You lose this round!")
        comp_wins += 1
        print("You chose", choice[user_choice - 1], "and the computer chose", choice[comp_choice - 1])
    print("You have", user_wins, "wins and the computer has", comp_wins, "wins")
    play_again = int(input("Do you want to play again? Type 1 for yes and 2 for no: "))
    return play_again

while play_again == 1:
    game()

print()
print("You have", user_wins, "wins and the computer has", comp_wins, "wins")
if user_wins > comp_wins:
    print("You are the overall winner!")
elif user_wins == comp_wins:
    print("Its a draw!")
else:
    print("The computer is the overall winner!")
print()
print("Thanks for playing!")
