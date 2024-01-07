#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from the arguments
    total = sum(int(arg) for arg in args)
    print(total)
