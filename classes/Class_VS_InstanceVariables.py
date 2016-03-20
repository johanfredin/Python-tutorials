"""
Tutorial on difference between class and instance variables
"""


class Girl:

    gender = "female"

    def __init__(self, name):
        self.name = name


girl = Girl("Rachel")
print(girl.gender)

# We can access name although its only declared in constructor
print(girl.name)
girl.name = "Rosa"
print(girl.name)