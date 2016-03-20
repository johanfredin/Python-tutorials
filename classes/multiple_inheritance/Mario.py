class Mario():
    def move(self):
        print('I am moving')

class Shroom():
    def eat_shroom(self):
        print("Now I am big")


# Inherits from both parents!
# We don't need anything so we write pass
class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.eat_shroom()
bm.move()