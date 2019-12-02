def check(guess, secret):
    '''Compare a guessed number against a secret number.

    Return True if game over (guessed or quit requested).
    '''

    if "Q" == guess:
        print("Good bye!")
        return True

    if guess < secret:
        print("No. Your guess was too low.")
        return False

    if guess > secret:
        print("No. Your guess was too high.")
        return False

    print("Correct! You guessed my number!")
    return True
