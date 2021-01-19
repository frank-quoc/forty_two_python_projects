import items, enemies, actions, world, player

class MapTile: # Abstract base classes never get instances of it created
    """An abstract base class for Tiles."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all moves for the action tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You're in the main tent of an evil circus. 
        There's no way to the front entrance because there's a giant wooly mammoth asleep blocking it.
        Got to find the back door, I guess.
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
            the_player.hp = the_player.hp - self.enemy.damage
            print(f"Enemy does {self.enemy.damage} damage. You have {the_player.hp} HP remaining.")
 
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyHousePath(MapTile):
    def intro_text(self):
        return """
        Nothing to see here. Just a clown eating a pie. Tip toe, so he doesn't notice you.
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
            You beat the two headed monkey until it ran away. 
            """

class ThreeTailedLigerRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ThreeTailedLiger())

    def  intro_text(self):
        if self.enemy.is_alive():
            return """
            It's a Liger with 3 tails. Is it from hell?
            """
        else:
            return """
            Well, you did it. The Liger was coaxed into playing with your ball of yarn.
            """   

class Find5RubiesRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dollars(5))

    def intro_text(self):
        return """
        Woot woot. You found 5 rubies on the ground. Today, is a lucky day. 
        Cept for the whole kidnapping thing.
        """
    
    def update_inv(self):
        player.Player.inventory[0] += self.items.Rubies(5)

class FindBallofYarnRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BallOfYarn())

    def intro_text(self):
        return """
        It's a ball of yarn. Hmmm, wonder what you could do with this?
        """

class LeaveHouseRoom(MapTile):
    def intro_text(self):
        return """
        You finally find the backdoor. Thank god.
        What happened? How did you end up here.?
        Well, at least you're free. Time to go to the police.
        Or, go home to sleep.
        """
 
    def modify_player(self, player):
        player.victory = True
