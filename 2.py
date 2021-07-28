class Clothes:

    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def coat(self):
        return self.size / 6.5 + 0.5

    @property
    def suit(self):
        return self.height * 2 + 0.3

    def textile(self):
        return self.coat + self.suit


c = Clothes(48, 179.5)
print(f'Расход ткани на пальто: {c.coat:.3f} м, расход ткани на костюм: {c.suit} м')
print(f'Общий расход ткани {c.textile():.3f} м')
