class Wolf():
    def __init__(self):
        self.age = 150
        self.color = "black"
        self.aggressivity = "high"
        self.pack = False
        self.favourite_snacks = "lamb"

    def howl(self):
        print("HOWL")

    def growl(self):
        print("grrr")

    def bark(self):
        print("WOOF WOOF")

wolfy = Wolf()
print(wolfy.favourite_snacks)
wolfy.bark()
wolfy.howl()

class Dog(Wolf):
    def __init__(self, training, breed):
        super().__init__()
        self.aggressivity = "low"
        self.breed = breed

        if training == "sedni":
            print("sedam")
        elif training == "aport":
            print("aportuji")

    def bark(self):
        print("woof woof")


doggy = Dog("sedni", "Border Colie")
doggy.bark()
print(doggy.breed)
