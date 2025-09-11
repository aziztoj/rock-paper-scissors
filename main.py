
# # #stretch task
# # print("Welcome to the Survival Game! Keep playing until you die!")
# # import random

# # player_hp = 100
# # level_counter = 1

# # while player_hp > 0:
# #     obstacle = random.randint(1, 3)
# #     if obstacle == 1:
# #         print("There is a bear in front of you")
# #         action = int(input("What do you want to do? Type 1 to run, type 2 to fight, type 3 to hide: "))
# #         if action == 1:
# #             player_hp -= random.randint(1, 10)
# #             print("You ran away but you're tired now")
# #             print("You have", player_hp, "HP left.")
# #             level_counter += 1
# #         elif action == 2:
# #             chance = random.randint(0, 100)
# #             if chance > 50:
# #                 print("You killed the bear")
# #                 player_hp -= random.randint(0, 20)
# #                 print("You have", player_hp, "HP.")
# #                 level_counter += 1
# #             else:
# #                 print("You didn't kill the bear and had to run away")
# #                 player_hp -= random.randint(20, 50)
# #                 print("You have", player_hp, "HP.")
# #                 level_counter += 1
# #         elif action == 3:
# #             chance = random.randint(0, 100)
# #             if chance > 60:
# #                 print("You hid from the bear")
# #                 print("You have", player_hp, "HP.")
# #                 level_counter += 1
# #             else:
# #                 print("The bear found you and killed you")
# #                 player_hp = 0

# #     elif obstacle == 2:
# #         print("There is a rock falling from the sky")
# #         action = int(input("Do you want to dodge left (type 1) or dodge right (type 2): "))
# #         if action == 1 or action == 2:
# #             chance = random.randint(0, 100)
# #             if chance > 50:
# #                 print("You dodged successfully")
# #                 level_counter += 1
# #             else:
# #                 print("You got hit by the rock")
# #                 player_hp -= random.randint(10, 20)
# #                 print("You have", player_hp, "HP.")

# #     elif obstacle == 3:
# #         print("There's a mysterious fruit in front of you")
# #         action = int(input("Do you want to eat the fruit (type 1) or just leave it (type 2): "))
# #         if action == 1:
# #             chance = random.randint(0, 100)
# #             if chance > 50:
# #                 print("You ate the fruit and gained health")
# #                 player_hp += random.randint(10, 20)
# #                 print("You have", player_hp, "HP.")
# #                 level_counter += 1
# #             else:
# #                 print("The fruit was poisonous and you died")
# #                 player_hp = 0
# #         elif action == 2:
# #             print("You decided to leave the fruit and continue on your way.")
# #             level_counter += 1

# # print("Thanks for playing this survival game! You completed ", level_counter+1, "levels")



# # # # # colour = ['red', 'orange','white']
# # # # # userinput1 = input()
# # # # # colour.remove(userinput1)
# # # # # userinput2 = input()
# # # # # colour.remove(userinput2)
# # # # # print(colour[0])

# # # # # userinput = input()
# # # # # ZX = []
# # # # # ZX.append(userinput)
# # # # # ZX = ZX[:100]
# # # # # p = list(''.join(ZX))
# # # # # good = False
# # # # # for i in range(len(p)-1):
# # # # #     if p[i] == p[i+1]:
# # # # #         good = False
# # # # #         break
# # # # #     else:
# # # # #         good = True

# # # # # if good == False:
# # # # #     print("BAD")
# # # # # else:
# # # # #     print("GOOD")

# # # # # ug = int(input())
# # # # # if ug > 79:
# # # # #     print("A")
# # # # #     exit()
# # # # # elif ug > 69:
# # # # #     print("B")
# # # # #     exit()
# # # # # elif ug > 59:
# # # # #     print("C")
# # # # #     exit()
# # # # # elif ug >49:
# # # # #     print("D")
# # # # #     exit()
# # # # # else:
# # # # #     print("F")
    

# # # # # userinput1 = input()
# # # # # list1 = []
# # # # # list1.append(userinput1)
# # # # # list11 = list(''.join(list1))
# # # # # list11.sort()


# # # # # userinput2 = input()
# # # # # list2 = []
# # # # # list2.append(userinput2)
# # # # # list21 = list(''.join(list2))
# # # # # list21.sort()

# # # # # if list11 == list21:
# # # # #   print("yes")
# # # # # else:
# # # # #   print("no")

# # # # # number = [1,2,3,4,5,6,7]
# # # # # newnumber = []
# # # # # for i in number:
# # # # #   newnumber.append(i**2)
# # # # # print(newnumber)

# # # # highestavg = 0
# # # # score = [[76,65,67],[32,90,75],[66,77,31]]
# # # # print(score)
# # # # physics_top = max(row[0] for row in score)
# # # # chemistry_top = max(row[1] for row in score)
# # # # biology_top = max(row[2] for row in score)
# # # # print("Highest in physics is", physics_top, "\nHighest in chemistry is", chemistry_top, "\nHighest in biology is", biology_top)

# # # # for student in score:
# # # #   avg = sum(student) / len(student)
# # # #   highestavg= max(highestavg, avg)

# # # # print("Highest average is", highestavg)

# # # load = input("Do you want to load the previous score? Y/N ").lower()
# # # if load == "n":
# # #   teamlist = []
# # #   points = []
# # #   for i in range(3):
# # #    team = input("Enter a team name ")
# # #     teamlist.append(team)

# # #   for team in range(3):
  
# # #     win = int(input("How many Wins did " + teamlist[team] + " get?"))
 
# # #     draws = int(input("How many draws did " + teamlist[team] + " get?"))

# # #     lose = int(input("How many loses did " +  teamlist[team] + " get?"))
              
# # #     points.append(win*3 + draws)
  
# # # print()
# # # else:
# # #   teamlist = ["Arsenal", "Chelsea", "Man UTD"]
# # #   FILE = open('footballtracker.txt', 'r')
# # #   for i in range(3):
# # #   points[i] = points[i] + int(FILE.readline(i))
  
  


# # # FILE = open('footballtracker.txt','w')
# # # for teampoints in range(3):
# # #   FILE.write(teamlist[teampoints] +  str(points[teampoints]) + "\n")
# # # FILE.close()


# # # n, k = map(int, input().split())
# # # correct_answers = input().strip()
# # # guessing_sequence = input().strip()
# # # correct_count = 0

# # # for i in range(n):
# # #     guessed_answer = guessing_sequence[i % k]
# # #     if guessed_answer == correct_answers[i]:
# # #         correct_count += 1

# # # print(correct_count)


# # # n, m, k, L = map(int,input().split())
# # # numberofsong = []
# # # for i in range(n):
# # #     numberofsong.append(i)

# # # while L>0:
# # #     k = k+m
# # #     if k>n:
# # #         k = k-n
# # #     L = L - 1
# # # print(k)


# # # n, m, k, l = map(int, input().split())

# # # final_position = (k - 1 + m * l) % n + 1

# # # print(final_position)

# # # number1 = int(input())
# # # number2 = int(input())
# # # product = number1 * number2
# # # print(product)
# # # print()

# # # num1 = int(input("Input a number 1 - 20 "))
# # # if 1 <= num1 <= 20:
# # #   print("number in range")
# # # else:
# # #   print("Number is not in range")
# # # print()

# # # for i in range(100,201): 
# # #   print(i)
# # # print()

# # # def name():
# # #   name = input("Input your name ")
# # #   print(name)
# # # name()

# # # score = float(input("Enter your test score out of 50: "))
# # # if score > 50 or score < 0:
# # #   print("Invalid score")
# # # else:
# # #   percentage = score / 50 * 100
# # #   print(f"your percentage is: {percentage:.2f}%")
# # #   if percentage > 90:
# # #     print("Outstanding")
# # #   elif percentage > 60:
# # #     print("Good Job")
# # #   else:
# # #    print("Work harder next time!")

# # # number = 1
# # # count1 = 0
# # # count2 = 0
# # # while number != 0:
# # #   number = int(input("input number between 10 and 20: "))
# # #   if number > 9 and number < 15:
# # #     count1 += 1
# # #   if number > 14 and number < 21:
# # #     count2 += 1
# # # print(count1,"numbers are between 10 and 14 (inclusive) and ", count2,"numbers between 15 and 20 (inclusive)")


# # # def randoms():
# # #   import random
# # #   number = random.randint(1,4)
# # #   return number
  
# # # x = randoms()

# # # user = int(input("Input a number: "))
# # # if x == 1:
# # #   print(user)
# # # elif x == 2:
# # #   print(user*10)
# # # elif x == 3:
# # #   print(user/2)
# # # else:
# # #   user = 0
# # #   print(user)
  


# import random
 
# options = [1,2,3] 
# play_again = 1
# user_wins = 0
# comp_wins = 0
# choice = ["rock", "scissors","paper"]

# print("Welcome to the rock scissors paper game! Do you know the rules?")
# rules_needed = input("Type y/n: ").lower()
# if rules_needed == "n":
#     print("Rock beats scissors, scissors beats paper, paper beats rock. If you play the same as the computer, its a draw. Good luck!")

# def game():
#     print()
#     global user_wins
#     global comp_wins
#     global play_again
#     print("CHOOSE EITHER ROCK (type 1), SCISSORS (type 2) OR PAPER (type 3)")
#     user_choice = int(input())
#     comp_choice = random.choice(options)
#     print(comp_choice)
#     if user_choice - comp_choice == -1 or user_choice - comp_choice == 2:
#         print("You win this round!")
#         print("You chose", choice[user_choice - 1], "and the computer chose", choice[comp_choice - 1])
#         user_wins += 1
#     elif user_choice == comp_choice:
#         print("Its a draw!")
#         print("You chose", choice[user_choice - 1], "and the computer chose", choice[comp_choice - 1])
#     else:
#         print("You lose this round!")
#         comp_wins += 1
#         print("You chose", choice[user_choice - 1], "and the computer chose", choice[comp_choice - 1])
#     print("You have", user_wins, "wins and the computer has", comp_wins, "wins")
#     play_again = int(input("Do you want to play again? Type 1 for yes and 2 for no: "))
#     return play_again

# while play_again == 1:
#     game()

# print()
# print("You have", user_wins, "wins and the computer has", comp_wins, "wins")
# if user_wins > comp_wins:
#     print("You are the overall winner!")
# elif user_wins == comp_wins:
#     print("Its a draw!")
# else:
#     print("The computer is the overall winner!")
# print()
# print("Thanks for playing!")

import random
print("Welcome to the Guess the Number Game! \nWhat is your name?")
name = input()
print("Hello", name, " \nI am thinking of a number between 1 and 20. Guess the number! You have 5 tries")
number = random.randint(1,20)
guess = int(input())
count = 1
while guess != number:
    if guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = int(input("Guess again: "))
    count += 1
    if count == 5 and guess != number:
        print("You have run out of tries")
        print("The number was", number)
        break
if guess == number:
    print("You guessed the number in", count,"tries")



