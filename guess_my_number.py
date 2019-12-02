'''guess_my_number.py - A simple number guessing game.

Computer picks a number, human tries to guess it.
'''

from random import randint
from prompt_for_guess import ask
from check_guess import check

print("I am thinking of a number between 1 and 10.")
secret = randint(1, 10)

print("Can you guess my number?")

game_over = False
while not game_over:
    guess = ask("\nWhat is your guess? (type 'q' to give up) : ")
    game_over = check(guess, secret)

print("Thank you for playing my game.")
