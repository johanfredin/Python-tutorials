"""
Example tutorial about how variable scope works in python
"""

# Both functions can access a
a = 7823

def corn():
    print(a)

def fudge():
    print(a)

corn()
fudge()