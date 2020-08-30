import random, sys

print("=========Number Guessing Game===========")

answer = random.randint(1,5)

print("Hello, I've thought of a number between 1 and 5. Can you guess what it is?")

guess = int(input("Guess the number: "))

def answer_question(guess):
    if guess == answer:
        print("Winner. Winner. Chicken Dinner!")
        sys.exit()
    elif guess > answer:
        print("Too high.")
        guess_again()
    elif guess < answer:
        print("Too low.")
        guess_again()      

def guess_again():
    print("Guess again")
    guess = int(input("Guess again: "))
    answer_question(guess)
    return guess

answer_question(guess)