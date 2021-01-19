class Item:
    """Base class for all the items."""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return f"{self.name}\n======\n{self.description}\nValue: {self.value}\n"

class Ruby(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='Ruby', description=f'A red color mineral that shines {str(self.amt)}.', 
            value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return f"{self.name}\n======\n{self.description}\nValue: {self.value}\nDamage: {self.damage}"

class BlackGlove(Weapon):
    def __init__(self):
        super().__init__(name='Black Glove', description=f'A black glove. You can glove-slap someone in the face', 
            value=0, damage=5)

class Bat(Weapon):
    def __init__(self):
        super().__init__(name='Bat', description=f'SWING batta batta SWING', value=10, damage=10)
