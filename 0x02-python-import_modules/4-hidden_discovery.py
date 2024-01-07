#!/usr/bin/python3.8
import dis
import sys

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
        instructions = dis.get_instructions(code)
        names = {instr.argval for instr in instructions if instr.opname == 'LOAD_CONST'}

        filtered_names = sorted(name for name in names if not name.startswith('__'))
        for name in filtered_names:
            print(name)
