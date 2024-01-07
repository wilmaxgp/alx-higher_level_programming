#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Exclude script name from argument count
    args = sys.argv[1:]  # Exclude the script name from the arguments list

    print("{} {}{}.".format(num_args, "argument" if num_args == 1 else "arguments", ":" if num_args > 0 else "."))
    
    if num_args > 0:
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
