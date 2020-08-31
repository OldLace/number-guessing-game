import random, sys

attempts = 0

answer = random.randint(1,10)

def answer_question(guess, attempts):
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
        answer_question(guess, attempts)
    except ValueError:
        print("Whole numbers only, please.")
        continue

answer_question(guess, attempts)