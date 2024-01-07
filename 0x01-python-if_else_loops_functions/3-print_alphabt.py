#!/usr/bin/python3
output = ''.join(chr(char) for char in range(97, 123) if chr(char) not in ['q', 'e'])
print(output, end='')
