import random, sys

attempts = 1

answer = random.randint(1,10)
print(attempts)
def answer_question(guess, attempts):
    print(attempts)
    if attempts > 2:
            print("You lose.")
            sys.exit()
    else:
        if guess == answer:
            print("Winner. Winner. Chicken Dinner!")
            sys.exit()
        elif guess > answer:
            print("Too high.")
            attempts = attempts + 1
            guess_again(attempts)
        elif guess < answer:
            print("Too low.")
            attempts = attempts + 1
            guess_again(attempts)      

def guess_again(attempts):
    guess = int(input("Guess again: "))
    answer_question(guess, attempts)
    return guess

print("=========Number Guessing Game===========")

print("Hello, I've thought of a number between 1 and 10. Can you guess what it is?")

while True:
    try:
        guess = int(input("Guess the number: "))
        if attempts > 3:
            print(attempts)
            print("You lose.")
            sys.exit()
        else:
            answer_question(guess, attempts)
    except ValueError:
        print("Whole numbers only, please.")
        continue

answer_question(guess, attempts)