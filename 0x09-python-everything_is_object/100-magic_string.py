#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, "n", -1) + 1; return ", ".join(["BestSchool"] * magic_string.n)
magic_string.n = 0
