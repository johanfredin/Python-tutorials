"""
Function with a default value example
"""
def get_gender(sex = 'Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender() # Will print Unknown
get_gender("m") # Will print Male
get_gender("f") # Will print female