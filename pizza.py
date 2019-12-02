from math import pi

# Ask the user for the size (diameter) of the pizza.
ans = input("How big is your pizza (diameter in inches)? ")
d = int(ans)

# Calculate the radius from the diameter.
r = d/2

# Calculate the area from the radius.
a = pi * r**2

# Display the result.
print("That is", round(a, 1), "square inches of cheesy goodness")