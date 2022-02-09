import random
import sys

# GAME SETUP

# Default values
low = 1
high = 10

# If user doesn't enter arguments
if len(sys.argv) != 3:
    print("Please run the program with two integer arguments where the first integer is less than the second integer.")
    print("Example: python randomgame.py 5 10")
    exit()

if len(sys.argv) == 3:
    # If user provides invalid arguments
    if (not ((sys.argv[1].isdigit() and sys.argv[2].isdigit()) or not (int(sys.argv[1]) < int(sys.argv[2])))):
        print("Please run the program with two integer arguments where the first integer is less than the second integer.")
        print("Example: python randomgame.py 5 10")
        exit()
    # If user provides valid arguments
    else:
        low = int(sys.argv[1])
        high = int(sys.argv[2])

# GAME PLAY

answer = random.choice(range(low, high+1))

def guess():
    return int(input(f"Guess a number between {low} and {high}: "))

user_guess = guess()

while user_guess != answer:
    user_guess = guess()

print("You guessed it!")