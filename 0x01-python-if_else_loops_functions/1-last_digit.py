#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    d = number % -10
else:
    d = number % 10

if d > 5:
    w = "and is greater than 5"
elif d == 0:
    w = "and is 0"
elif d < 6:
    w = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, d, w))
