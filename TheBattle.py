from ThePlayer import Player
from TheGame import Game
# Battle for the player


class Battle:
    def __init__(self, p1: Player, p2: Player, game: Game) -> None:
        self.p1 = p1
        self.p2 = p2
        self.game = game

    def the_battle(self) -> None:
        print(f"You ({self.p1.username}) VS {self.p2.username} in {self.game.stage_num}.{self.game.round_num}")
        print(f"Your field: {self.p1.field.list_agents()}")
