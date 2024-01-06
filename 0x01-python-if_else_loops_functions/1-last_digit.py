#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digt = (number) % 10
if number < 0:
    last_digt *= -1
if last_digt > 5:
    print(f"{number:d} is {last_digt:d} and is greater than 5")
elif last_digt == 0:
    print(f"{number:d} is {last_digt:d} and is 0")
else:
    print(f"{number:d} is {last_digt:d} and is less than 6 and not 0")
