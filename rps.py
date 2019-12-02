from random import randint

def rps():
    '''return a random pick of rock, paper, or scissors'''

    pick = randint(1, 3)

    if 1 == pick:
        return "rock"

    if 2 == pick:
        return "paper"

    if 3 == pick:
        return "scissors"