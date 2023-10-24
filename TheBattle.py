from ThePlayer import Player
from TheGame import Game
# Battle for the player


def battle_result(p1: Player, p2: Player) -> int and bool:
    difference = p1.field.total_power() - p2.field.total_power()
    result = None
    if difference > 0:
        p1.result = True
        p2.result = False
        result = True
    elif difference < 0:
        p1.result = False
        p2.result = True
        result = False
    return difference, result


class Battle:
    def __init__(self, p1: Player, p2: Player, game: Game) -> None:
        self.p1 = p1
        self.p2 = p2
        self.game = game

    def the_battle(self) -> None:
        print(f"You ({self.p1.username}) VS {self.p2.username} in {self.game.stage_num}.{self.game.round_num}")
        print(f"Your field: {self.p1.field.list_agents()}")
        print(f"Their field: {self.p2.field.list_agents()}")
        difference, result = battle_result(self.p1, self.p2)
        if result is True:
            print(f"You won! {self.p2.username} lost {difference} hp.")
        elif result is False:
            print(f"You lost. You lost {difference} hp.")
        else:
            print(f"You tied.")
