from math import pi

def input_int(prompt):
    '''Prompt for input, return the int value.'''
    ans = input(prompt)
    return int(ans)

def circle_area(diameter):
    '''Return the area of a circle calculated from its diameter.'''
    radius = diameter/2
    area = pi * radius**2
    return area

d = input_int("How big is your pizza (diameter in inches)? ")
a = circle_area(d)
print("That is", round(a, 1), "square inches of cheesy goodness")