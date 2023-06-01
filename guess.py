
import random

number = random.randint(1, 10)
user_guess = int(input("Kindly guess a number between 1 and 10: "))
chance = 5


while chance !=0:
    chance -= 1
    if user_guess != number and user_guess < number and chance != 0:
        print("Guess is lower than number")
        user_guess = int(input("Kindly guess a higher number: "))
    elif user_guess != number and user_guess > number and chance != 0:
        print("Guess is higher than number")
        user_guess = int(input("Kindly guess a lower number: "))
    elif user_guess != number and chance == 0:
        print("You have exhausted your chances")
    else:
        print(f"Congrats your guess {user_guess} is correct")
        chance = 0



