import random
import getpass
#1
options = [1,2,3] 
play_again = 1
user_wins = 0
comp_wins = 0
choice = ["rock", "scissors","paper"]
name1 = ""
name2 = ""
user1choice = 0
user2choice = 0
user1wins = 0
user2wins = 0

#creating a new file to record the game if playing against another player
with open("record.txt", "w") as file:
    file.write("This is the record of the game: \n")
file.close()

#welcoming the user and asking if they need the rules
print("Welcome to the rock scissors paper game! What is your name?")
name1 = input("Type your name: ")
print("\nHello " + str(name1) + ". Do you know the rules?")
rules_needed = input("Type y/n: ").lower()
if rules_needed == "n":
    print("Rock beats scissors, scissors beats paper, paper beats rock. If you play the same as the computer, its a draw. Good luck!\n")

#code for game against computer
def compgame():
    print()
    global user_wins
    global comp_wins
    print("CHOOSE EITHER ROCK (type 1), SCISSORS (type 2) OR PAPER (type 3)")
    user_choice = int(input())
    comp_choice = random.choice(options)
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
    print("------------------------------------------------------------------")
 

#code for game against another player
def userplay():
    global name1
    global name2
    global user1choice
    global user2choice
    global user1wins
    global user2wins
    global file
    print()
    print(name1, "pick either ROCK(1), SCISSORS(2) or PAPER(3):")
    user1choice = int(getpass.getpass(""))
    print(name2, "pick either ROCK(1), SCISSORS(2) or PAPER(3): ")
    user2choice = int(getpass.getpass(""))
    if user1choice - user2choice == -1 or user1choice - user2choice == 2:
        print(name1, "wins this round!")
        with open("record.txt", "a") as file:
            file.write(name1 + " won the round!\n")
        file.close()
        print("You chose", choice[user1choice - 1], "and", name2, "chose", choice[user2choice - 1],"\n")
        user1wins += 1
    elif user1choice == user2choice:
        print("Its a draw!")
        with open("record.txt", "a") as file:
            file.write("Its was a draw!\n")
        file.close()
        print(name1, "chose", choice[user1choice - 1], "and", name2, "chose", choice[user2choice - 1],"\n")
    else:
        print(name2, "wins this round!")
        with open("record.txt", "a") as file:
            file.write(name2 + " won the round!\n")
        file.close()
        print(name1, "chose", choice[user1choice - 1], "and", name2, "chose", choice[user2choice - 1],"\n")
        user2wins +=1 
    print(name1, "has", user1wins, "wins and", name2, "has", user2wins, "wins")
    print("------------------------------------------------------------------")

#asking if they want to play against the computer or another player
print("\nDo you want to play against the computer or against another player?")
print("Type 1 for computer and 2 for another player")
play_against = int(input())

if play_against == 2:
    print("Player 2, enter your name: ")
    name2 = input()

print("\nHow many rounds do you want to play?")
rounds = int(input("Type the number of rounds: "))

#looping the game for the number of rounds the user wants to play
if play_against == 1:
    for i in range(rounds):
        compgame()
else:
    for i in range(rounds):
        userplay()
        
#display winner against computer
if play_against == 1:
    
    print()
    print("You have", user_wins, "wins and the computer has", comp_wins, "wins")
    if user_wins > comp_wins:
        print("You are the overall winner!")
    elif user_wins == comp_wins:
        print("Its a draw!")
    else:
        print("The computer is the overall winner!")
    print()
    
#display winner against another player
else:
    print()
    if user1wins > user2wins:
        print(name1, "is the overall winner!")
    elif user1wins == user2wins:
        print("Overall, its a tie!")
    else:
        print(name2, "is the overall winner!")
    print()
    with open("record.txt", "r") as file:
        print(file.read())    
    print()

print("Thanks for playing!")