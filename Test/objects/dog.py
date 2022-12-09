class Dog:
    def __init__(self, name, age, breed="unknown"):
        self.name = name
        self.age = age
        self.breed = breed
        self.aggi = 50

    def protect(self):
        if self.aggi > 75:
            print(f"{self.name}: Grrrr")
        print(f"{self.name}: Woof")
        self.aggi += 10

    def calm(self):
        if self.aggi < 5:
            print(f"{self.name}: Zzzzz")
        print(f"{self.name}: :)")
        self.aggi -= 10


d1 = Dog("bob", 2, "Collie")
d2 = Dog("jack", 4, "Jack Russel")

d1.protect()

print(f"{d1.name}:{d1.aggi}% aggression")
print(f"{d2.name}:{d2.aggi}% aggression")