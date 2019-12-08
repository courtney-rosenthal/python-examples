DIE_IMAGES = {
  1: "+---+\n|   |\n| o |\n|   |\n+---+",
  2: "+---+\n|o  |\n|   |\n|  o|\n+---+",
  3: "+---+\n|o  |\n| o |\n|  o|\n+---+",
  4: "+---+\n|o o|\n|   |\n|o o|\n+---+",
  5: "+---+\n|o o|\n| o |\n|o o|\n+---+",
  6: "+---+\n|o o|\n|o o|\n|o o|\n+---+",
}

def die(roll):
    '''Return a string that will print for a die rolled 1 thru 6. Throws KeyError on bad argument.'''
    return DIE_IMAGES[int(roll)]
