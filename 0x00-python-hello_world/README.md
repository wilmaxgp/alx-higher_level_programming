# 0x00. Python - Hello, World

# 0. Run Python file
Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable $PYFILE
using this files samples,
-guillaume@ubuntu:~/py/0x00$ cat main.py 
-#!/usr/bin/python3
-print("Best School")
-guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
-guillaume@ubuntu:~/py/0x00$ ./0-run
-Best School
_guillaume@ubuntu:~/py/0x00$

#1. Run inline
Write a Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE
