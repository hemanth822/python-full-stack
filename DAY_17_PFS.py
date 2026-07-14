'''

                                DAY 17 - PYTHON CONCEPTS

Modules:
----------
-> A module is a python file (.py) that contains reusable code
1.Variables
2.Functions
3.Classes
4.Objects
5.Statements

why this
----------
-> Instead of writing the same code repeatedly, we can store it in a module and use it whenever needed......

Type of modules:
-----------------
1.user-define
2.Built-in

1.user-define:
---------------
-> we can define our own module and use it another codes or files
ex:
'''
import ekanth # alraedy created a file with name ekanth.py and it was imported.
print(ekanth.add(20,2))
print(ekanth.sub(20,2))
print(ekanth.mul(20,2))
print(ekanth.div(20,2))

'''
Import specific function:
---------------------------
ex:
'''
from ekanth import add
print(ekanth.add(20,2))

from ekanth import *
print(ekanth.sub(20,2))
'''
using alias:
--------------
ex:
'''
import ekanth as ev
print(ev.add(20,2))
'''
ex:
'''
import ekanth
print(ekanth.power(2,3))
print(ekanth.floordiv(3,2))

'''
2.Built-in:
-------------
1.math
2.os
3.sys
4.random

1.math
---------
sqrt()      -> square root
factorial() -> factorial
pow()       -> power
ceil()      -> round up
pi          -> pi value
ex:
'''
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,5))
print(math.pi)

'''
2.os:
------
-> The os module is used to interact with operating system
getcwd() -> current directory
mkdir()  -> to create directory
rmdir()  -> to remove directory

ex:
'''
import os
print(os.getcwd())
os.mkdir("ekanthv")
os.rmdir("ekanthv")
'''
3.sys:
-------
-> To  provide the information about python interpeter
ex:
'''
import sys
print(sys.version)

'''
4.Random:
----------
-> Used to generate random values
ex:
'''
import random
print(random.randint(1000,9999))

colors = ['Red','Blue','Green','yellow']
print(random.choice(colors))
