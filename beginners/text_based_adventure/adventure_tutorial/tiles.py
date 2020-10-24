import items, enemies

class MapTile: # Abstract base classes never get instances of it created
    """An abstract base class for Tiles."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You wake up on the floor of your ex's living room. If you never had one, just use your imagination.
        She's not around. The room is dark and for the dining room table is smashed to pieces.
        """

    def modify_player(self, player):
        # Room has no effect on the player.
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)
    
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp -= self.enemy.damage
            print(f"Enemy does {self.enemy.damage}. You have {the_player.hp} HP left.")

class EmptyHousePath(MapTile):
    def __init__(self):
        return """
        Nothing to see here. Just a dead body. Walk over it.
        """
        
    def modify_player(self, player):
        # Room has no effect on the player.
        pass

class TwoHeadedMonkeyRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.TwoHeadedMonkey())

    def  intro_text(self):
        if self.enemy.is_alive():
            return """
            What the... Why is there a two-headed monkey. It jumps at you.
            """
        else:
            return """
            You beat the two headed monkey until it ran away. No animals were killed in the making of this game.
            """

class EvilGrampaJoesRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.EvilGrampaJoe())

    def  intro_text(self):
        if self.enemy.is_alive():
            return """
            Man. It's your exes Grampa Joe. You hated him. He's using his cane to wack you again.
            """
        else:
            return """
            Well, you did it. You put Grampa Joe in a coma. He was a jerk anyways.
            """   

class FindBlackGloveRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BlackGlove())

    def intro_text(self):
        return """
        There's no weapons in the room. Guess this random, petite black glove will do.
        """

class FindBat(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Bat())

    def intro_text(self):
        return """
        It's your favorite bat. You knew it. Your ex stole it to spite you. So, petty.
        """

