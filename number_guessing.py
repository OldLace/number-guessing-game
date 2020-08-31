import random, sys

print("=========Number Guessing Game===========")

answer = random.randint(1,5)

attempts = 0

print("Hello, I've thought of a number between 1 and 5. Can you guess what it is?")

guess = int(input("Guess the number: "))

def answer_question(guess, attempts):
    if guess == answer:
        print("Winner. Winner. Chicken Dinner!")
        sys.exit()
    elif guess > answer:
        print("Too high.")
        attempts = attempts + 1
        print(attempts)
        guess_again()
    elif guess < answer:
        print("Too low.")
        attempts = attempts + 1
        print(attempts)
        guess_again(attempts)      

def guess_again(attempts):
    print("Guess again") 
    guess = int(input("Guess again: "))
    answer_question(guess, attempts)
    return guess, attempts

answer_question(guess, attempts)


