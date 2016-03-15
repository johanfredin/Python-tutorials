"""
Example of how to use an undefined amount of arguments in python
"""

# does not have to be named args but its common practise, the * sign is mandatory tough
def add_numbers(caller, *args):
    total = 0
    for num in args:
        total += num
    print(caller, "I am done")
    return total

# First argument is normal argument, second is dynamic args
print(add_numbers("Johan", 1,2,3,4,5,6,7))

