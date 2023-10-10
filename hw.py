#
#
#

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        pass
    @staticmethod
    def create_animal(animal_type, name, species, **kwargs):
        if animal_type == "Fish":
            return Fish(name, species, **kwargs)
        elif animal_type == "Bird":
            return Bird(name, species, **kwargs)
        elif animal_type == "Mammal":
            return Mammal(name, species, **kwargs)
        else:
            raise ValueError("Unknown animal type")

class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__init__(name, species)
        self.water_type = water_type
    def make_sound(self):
        return "Bul' Bul'"
    def swim(self):
        return f"{self.name} is swimming in {self.water_type} water."

class Bird(Animal):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly
    def make_sound(self):
        return "Chirick Chirick"
    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying."
        else:
            return f"{self.name} cannot fly."

class Mammal(Animal):
    def __init__(self, name, species, num_legs):
        super().__init__(name, species)
        self.num_legs = num_legs
    def make_sound(self):
        return "Moo"
    def walk(self):
        return f"{self.name} is walking on {self.num_legs} legs."

if __name__ == "__main__":
    fish = Animal.create_animal("Fish", "Ariel'", "Goldfish", water_type="freshwater")
    eagle = Animal.create_animal("Bird", "Kesha", "Parrot", can_fly=True)
    cat = Animal.create_animal("Mammal", "Murka", "Cow", num_legs=4)

    print(fish.make_sound())
    print(fish.swim())
    print(eagle.make_sound())
    print(eagle.fly())
    print(cat.make_sound())
    print(cat.walk())
