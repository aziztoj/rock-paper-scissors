import random
import getpass
#1
options = [1,2,3] 
play_again = 1
play_against = 0
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
    global user1wins
    global user2wins
    global file
    print("CHOOSE EITHER ROCK (type 1), SCISSORS (type 2) OR PAPER (type 3)")
    name2 = "Computer"
    user1choice = 0
    while user1choice != 1 and user1choice != 2 and user1choice != 3:
        user1choice = int(input())
        if user1choice != 1 and user1choice != 2 and user1choice != 3:
            print("Invalid input, please try again")
            user1choice = int(input())
            continue
        else:
            break
        break
        
    user2choice = random.choice(options)
    if user1choice - user2choice == -1 or user1choice - user2choice == 2:
        result = "You win"
        user1wins += 1
        
    elif user1choice == user2choice:
        result = "Its a draw!"
        
    else:
        result = "Computer wins"
        user2wins += 1


    print(result)
    print("You chose", choice[user1choice - 1], "and the computer chose", choice[user2choice - 1])
    print("You have", user1wins, "wins and the computer has", user2wins, "wins")
    print("------------------------------------------------------------------")
    with open("record.txt", "a") as file:
        file.write(f"{name1}: {choice[user1choice-1]} | {name2}: {choice[user2choice-1]} | result: {result}  \n")

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
    user1choice = 0
    while user1choice != 1 and user1choice != 2 and user1choice != 3:
        user1choice = int(getpass.getpass(""))
        if user1choice != 1 and user1choice != 2 and user1choice != 3:
            print("Invalid input, please try again")
            continue
        else:
            break
        break
        
    print(name2, "pick either ROCK(1), SCISSORS(2) or PAPER(3): ")
    user2choice = 0
    while user2choice != 1 and user2choice != 2 and user2choice != 3:
        user2choice = int(getpass.getpass(""))
        if user2choice != 1 and user2choice != 2 and user2choice != 3:
            print("Invalid input, please try again")
            continue
        else:
            break
        break

    if user1choice - user2choice == -1 or user1choice - user2choice == 2:
        result = f"{name1} wins this round!"
        user1wins += 1
        
    elif user1choice == user2choice:
        result = "Its a draw!"
        
    else:
        result = f"{name2} wins this round!"
        user2wins +=1 

    print(result)
    print(name1, "chose", choice[user1choice - 1], "and", name2, "chose", choice[user2choice - 1],"\n")
    print("------------------------------------------------------------------")
    
    with open("record.txt", "a") as file:
        file.write(f"{name1}: {choice[user1choice-1]} | {name2}: {choice[user2choice-1]} | result: {result} \n")
        

#asking if they want to play against the computer or another player
print("\nDo you want to play against the computer or against another player?")
print("Type 1 for computer and 2 for another player")


while play_against != 1 and play_against != 2:
    play_against = int(input())
    if play_against != 1 and play_against != 2:
        print("Invalid mode, please type '1' or '2'")
        continue
    else:
        break
    break



if play_against == 2:
    with open("record.txt", "a") as file:
        file.write("MODE: 2 players \n")
    print("Player 2, enter your name: ")
    name2 = input()
else:
    with open("record.txt", "a") as file:
        file.write("MODE: Computer \n")

print("\nHow many rounds do you want to play?")
rounds = int(input("Type the number of rounds: "))


#looping the game for the number of rounds the user wants to play
if play_against == 1:
    for i in range(rounds):
        name2 = "computer"
        compgame()
else:
    for i in range(rounds):
        userplay()
        


#display winner 
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