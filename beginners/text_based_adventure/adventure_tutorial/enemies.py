class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class TwoHeadedMonkey(Enemy):
    def __init__(self):
        super().__init__(name='Two Headed Monkey', hp=10, damage=2)

class EvilGrampaJoe(Enemy):
    def __init__(self):
        super().__init__(name='Evil Grampa Joe', hp=30, damage=15)

