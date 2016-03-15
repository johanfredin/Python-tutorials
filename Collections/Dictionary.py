classmates = {"Tony": "cool but smells", "Johan": "I have my doubts"}

print(classmates)

print(classmates.get("Tony"))  # Get the value of tony
print(classmates["Johan"], "\n")  # Get the value of Johan


def print_classmates(dict):
    # Print all values
    for k, v in dict.items():
        print(k, v)
    print("\n")


print_classmates(classmates)

classmates.__setitem__("Johan", "Is not cool")

# Johan Will now be updated


print_classmates(classmates)
