from dog import Dog


class Kennel:

    def __init__(self, dog):
        self.occupant = dog

    def intruder(self):
        self.occupant.protect()


d1 = Dog("bob", 2, "Collie")
K = Kennel(d1)
K.intruder(d1)


print(f"{d1.occupant.name}: {d1.occupant.aggi}%")