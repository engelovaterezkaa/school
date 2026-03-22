class Car: #nemusime dedit ze sprite
    def __init__(self, color, name, wheel_count): #tady prijimame z konstrukteru
        self.color = color #uzivatel muze dopsat, ""= staticka hodnota
        self.name = name
        self.wheel_count = wheel_count
        self.has_steering_wheel = True
        self.stick = "manual"
    
    def honk(self):
        print(f"{self.name} Tůů tůůt")
    
    def open_door(self, door):
        print(f"{door} door is open")


porsche = Car("red", "911", 5) #musi se ulozit pod nejakou promennou

print(porsche.stick)
porsche.honk() #zavolame v ramci classy
porsche.open_door("front")

lambo = Car("yellow", "huracan", 4)
lambo.honk()


class Future_car(Car):
    def __init__(self, color, name, wheel_count, rockets):
        super().__init__(color, name, wheel_count)
        self.rockets = rockets
        self.has_steering_wheel = False
        self.stick = "automatic"
    
    def firework(self):
        print(f"{self.name} fires {self.rockets} rockets")

multipla_v2 = Future_car("blue", "Multipla", 7, 12)

print(multipla_v2.color)
multipla_v2.honk()

multipla_v2.firework()