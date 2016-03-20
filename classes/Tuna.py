class Tuna:

    age = 0

    # This is the constructor
    def __init__(self, age=5):
        self.age = age

    def swim(self):
        print("I am swimming")

    def getAge(self):
        return self.age

maTuna = Tuna()
print(maTuna.age)