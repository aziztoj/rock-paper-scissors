print("Welcome to the Survival Game! Keep playing until you die!")
import random

player_hp = 100
level_counter = 1

while player_hp > 0:
    obstacle = random.randint(1, 3)
    if obstacle == 1:
        print("There is a bear in front of you")
        action = int(input("What do you want to do? Type 1 to run, type 2 to fight, type 3 to hide: "))
        if action == 1:
            player_hp -= random.randint(1, 10)
            print("You ran away but you're tired now")
            print("You have", player_hp, "HP left.")
            level_counter += 1
        elif action == 2:
            chance = random.randint(0, 100)
            if chance > 50:
                print("You killed the bear")
                player_hp -= random.randint(0, 20)
                print("You have", player_hp, "HP.")
                level_counter += 1
            else:
                print("You didn't kill the bear and had to run away")
                player_hp -= random.randint(20, 50)
                print("You have", player_hp, "HP.")
                level_counter += 1
        elif action == 3:
            chance = random.randint(0, 100)
            if chance > 60:
                print("You hid from the bear")
                print("You have", player_hp, "HP.")
                level_counter += 1
            else:
                print("The bear found you and killed you")
                player_hp = 0

    elif obstacle == 2:
        print("There is a rock falling from the sky")
        action = int(input("Do you want to dodge left (type 1) or dodge right (type 2): "))
        if action == 1 or action == 2:
            chance = random.randint(0, 100)
            if chance > 50:
                print("You dodged successfully")
                level_counter += 1
            else:
                print("You got hit by the rock")
                player_hp -= random.randint(10, 20)
                print("You have", player_hp, "HP.")

    elif obstacle == 3:
        print("There's a mysterious fruit in front of you")
        action = int(input("Do you want to eat the fruit (type 1) or just leave it (type 2): "))
        if action == 1:
            chance = random.randint(0, 100)
            if chance > 50:
                print("You ate the fruit and gained health")
                player_hp += random.randint(10, 20)
                print("You have", player_hp, "HP.")
                level_counter += 1
            else:
                print("The fruit was poisonous and you died")
                player_hp = 0
        elif action == 2:
            print("You decided to leave the fruit and continue on your way.")
            level_counter += 1

print("Thanks for playing this survival game! You completed ", level_counter+1, "levels")
