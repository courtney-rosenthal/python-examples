'''guess_your_number.py - Computer runs a smart algorithm to guess your number.'''

def game():
    '''Run the "guess your number" game, returning number of guesses made.
    Returns number < 0 if game was terminated early.
    '''

    # Define the limits of the guessing game.
    min = 1
    max = 10

    # Counter for number of guesses made
    guesses = 0

    # Prompt the user to begin
    print("Pick a number between", min, "and", max)
    print("Let's see if I can guess your number.")
    input("Press the ENTER key after you pick a number, then we'll start : ")

    # This condition is called a "loop invariant".
    # An invariant is something that has to be true whenever we are in the loop.
    while min < max:

        # Print a blank line to start off the next round.
        # ^^^ this is a good comment, it explains why this lone print() appears
        print()

        # Make the next guess <-- bad comment (obvious)
        # Next guess is midway between the min and max values. <-- good comment
        guesses = guesses + 1
        guess = int((min+max)/2)
        print("I guess:", guess)

        ans = input("Am I C)orrect, H)igh, or L)ow? (type Q to give up and quit) : ")
        ans = ans.upper()

        if ans == 'Q':
            return -1

        if ans == 'C':
            print("Yay! I guessed your number.")
            return guesses

        if ans == 'H':
            max = guess - 1
        elif ans == 'L':
            min = guess + 1
        else:
            print("I did not understand your answer. Please try again.")

    # End condition has been reached, invariant (min < max) no longer true.
    if max == min:
        print("I know! Your number is", max)
        return guesses

    # Something went wrong. User probably gave us a bad response.
    print("I give up. I can't guess your number.")
    return -1

# Run the game.
guesses = game()
if guesses > 0:
    print("I guessed your number in", guesses, "guesses.")
print("Thank you for playing my game.")