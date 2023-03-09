'''
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random

exit = ''
randint = random.randrange(1, 10)
count = 0

while exit != 'exit':
    user = int(input("Pick a number between 1 and 9... "))
    if user < 0 or user > 9:
        print("Guess between 1 and 9")
        count += 1
        continue
    if randint > user:
        print("Too low")
    elif randint < user:
        print("Too high")
    elif randint == user:
        count += 1
        print("Just right!")
        print("Thanks for playing!")
        break
    count += 1
    exit = input("Keep guessing? Hit any key!  --  Or type 'exit' to quit \n")

print("You played",count,"times!")