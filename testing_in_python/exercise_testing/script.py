import random

def run_guess(guess, answer):
    try:
        if 1 <= guess <= 10:
            if guess == answer:
                print('You got it!')
                return True
        else:
            print('Please enter a number between 1 and 10')
    except TypeError as e:
        return False

if __name__ == '__main__':    
    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('Please enter a number between 1 and 10')
            continue