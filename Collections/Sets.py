"""
Shows the difference between a set and a list, a set can ONLY have unique values
first collection is a set, the second a list
"""

groceries_set = {"cereal", "milk", "starcrunch", "beer", "duct tape", "lotion", "beer"}
groceries_list = ["cereal", "milk", "starcrunch", "beer", "duct tape", "lotion", "beer"]
print(groceries_set)
print(groceries_list)

# Check if the set contains smt (also works for the list
if "milk" in groceries_set:
    print("milk in yall")

