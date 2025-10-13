import random
import getpass
#1
options = [1,2,3] 
play_again = 1
result = ""
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
p1 = 0
p2 = 0

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

def validinput():
    global user1choice
    while user1choice != 1 and user1choice != 2 and user1choice != 3:
        user1choice = int(getpass.getpass(""))
        if user1choice != 1 and user1choice != 2 and user1choice != 3:
            print("Invalid input, please try again")
            continue
        else:
            break
    return user1choice


def savegame(name1, p1, name2, p2, result):
    with open("record.txt", "a") as file:
        file.write(f"{name1}: {choice[p1-1]} | {name2}: {choice[p2-1]} | result: {result} \n")
        

#code for game against computer
def compgame():
    print()
    global user1wins, user2wins, user1choice, user2choice,name2, result,p1,p2
    
    print("CHOOSE EITHER ROCK (type 1), SCISSORS (type 2) OR PAPER (type 3)")
    name2 = "Computer"
    user1choice = 0
    validinput()
    p1 = user1choice
    
    p2 = random.choice(options)
    user2choice = p2
    if p1 - p2 == -1 or p1 - p2 == 2:
        result = "You win"
        user1wins += 1
        
    elif p1 == p2:
        result = "Its a draw!"
        
    else:
        result = "Computer wins"
        user2wins += 1

    print(result)
    print("You chose", choice[p1 - 1], "and the computer chose", choice[p2 - 1])
    print("You have", user1wins, "wins and the computer has", user2wins, "wins")
    print("------------------------------------------------------------------")
    return p1,p2,result

    

#code for game against another player
def userplay():
    global name1, name2, user1choice, user2choice,user1wins,user2wins,result,p1,p2
    
    print()
    print(name1, "pick either ROCK(1), SCISSORS(2) or PAPER(3):")
    user1choice = 0
    validinput(user1choice)
    p1 = user1choice

    
    print(name2, "pick either ROCK(1), SCISSORS(2) or PAPER(3): ")
    validinput()
    p2 = user1choice
    user2choice = p2

    if p1 - p2 == -1 or p1 - p2 == 2:
        result = f"{name1} wins this round!"
        user1wins += 1
        
    elif p1 == p2:
        result = "Its a draw!"
        
    else:
        result = f"{name2} wins this round!"
        user2wins +=1 

    print(result)
    print(name1, "chose", choice[p1 - 1], "and", name2, "chose", choice[p2 - 1],"\n")
    print("------------------------------------------------------------------")

        

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
        savegame(name1, user1choice, name2, user2choice,result)
else:
    for i in range(rounds):
        userplay()
        savegame(name1, user1choice, name2, user2choice, result)
        


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