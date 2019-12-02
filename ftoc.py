'''ftoc.py - Fahrenheit to Celsius temperature converter'''

def f_to_c(f):
    c = (f - 32) * (5/9)
    return c

def input_float(prompt):
    ans = input(prompt)
    return float(ans)

f = input_float("What is the temperature (in degrees Fahrenheit)? ")
c = f_to_c(f)

print("That is", round(c, 1), "degrees Celsius")