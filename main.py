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
