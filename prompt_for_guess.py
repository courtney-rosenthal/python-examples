def ask(prompt):
    '''Get a number from the user.'''

    while True:
        ans = input(prompt)

        if ans.upper().startswith("Q"):
            return "Q"

        if ans.isdigit():
            return int(ans)

        print("Sorry, invalid response. Please try again.")