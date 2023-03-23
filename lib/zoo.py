from lib.animal import Animal


class Zoo:

    all = []

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def animals(self):
        # new_animals = []
        # for animal in Animal.all:
        #     if animal.zoo == self:
        #         new_animals.append(animal)
        # return new_animals
        return [a for a in Animal.all if a.zoo == self]

    @property
    def animal_species(self):
        return {a.species for a in self.animals}

    def find_by_species(self, species):
        return [a.nickname for a in self.animals if a.species == species]

    @property
    def animal_nicknames(self):
        return [a.nickname for a in self.animals]

    @classmethod
    def find_by_location(cls, location):
        return [zoo.name for zoo in cls.all if zoo.location == location]
