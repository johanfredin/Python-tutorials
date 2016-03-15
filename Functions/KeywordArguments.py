"""
Example of keyword arguments
"""


def dumb_sentence(name = "Bucky", action = "ate", item = "tuna"):
    print(name, action, item)

dumb_sentence() # Will print "Buxky ate tuna"
dumb_sentence("Sally", "farts", "gently")

# We can alter the default function parameters when we call the function!
# This will print "Bucky is awesome"
dumb_sentence(item='awesome', action='is')