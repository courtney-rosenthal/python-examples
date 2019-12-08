from random import randint
from die_image import die
a = randint(1, 6)
print(die(a))
b = randint(1, 6)
print(die(b))
print("You rolled", a+b)
