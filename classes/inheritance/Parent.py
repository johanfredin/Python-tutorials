class Parent():

    def print_last_name(self):
        print("Roberts")


# Child inherits everything from parent by passing it into its parentheses
class Child(Parent):

    def print_first_name(self):
        print("Bucky")

    # Overrides parents method
    def print_last_name(self):
        print("Hahaha you are overriden!")


bucky = Child()
bucky.print_first_name()

# We can access the parents methods!
bucky.print_last_name()
