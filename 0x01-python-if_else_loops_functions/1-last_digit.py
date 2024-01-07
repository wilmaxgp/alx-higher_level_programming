#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
"""
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line
"""
last_digt = abs(number) % 10

if number == 0:
    last_digt = 0
elif number > 0:
    last_digt = last_digt
else:
    last_digt = -1

if last_digt > 5:
    strg = "the string and is greater than 5"
elif last_digt == 0:
    strg = "the string and is 0"
elif last_digt < 6 and last_digt != 0:
    strg = "the string and is less than 6 and not 0"

print(f"Last digit of {number:d} is {last_digt} {strg}") 
