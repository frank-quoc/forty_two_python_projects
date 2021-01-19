class Item:
    """Base class for all the items."""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return f"{self.name}\n======\n{self.description}\nValue: {self.value}\n"

class Rubies(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='Dollars', description=f'You have {str(self.amt)} dollars. Money Money.', 
            value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return f"\n{self.name}\n======\n{self.description}\nValue: {self.value}\nDamage: {self.damage}"

class Banana(Weapon):
    def __init__(self):
        super().__init__(name='Banana', description=f'Maybe the enemy can slip on this.', 
            value=0, damage=5)

class BallOfYarn(Weapon):
    def __init__(self):
        super().__init__(name='Ball of Yarn', description=f'Do you throw this at the enemy?', value=10, damage=10)
