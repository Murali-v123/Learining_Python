import random
from math import sqrt

import wikipedia

from package1 import greeting
from package2.subpackage import hello

hello.hello("murali")


print("Hello world")
greeting.greet("murali")


print(sqrt(36))  # No need to write math.sqrt()


print(random.randint(1, 10))  # Random number between 1 and 10

print(wikipedia.summary("Virat Kohli"))
