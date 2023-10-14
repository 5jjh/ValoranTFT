from ThePlayer import Player
from StoresPerLevel import StoreAndLevel as Spl
from random import randint
# Runs the game


class Game(object):
    def __init__(self) -> None:
        the_p = Player()
        self.stage_num = 1
        self.round_num = 1
        self.players = [the_p]

    def make_players(self) -> None:
        for i in range(2, 9):
            player_name = "p" + str(i)
            player_name = Player(username=player_name)
            self.players.append(player_name)
        return

    def make_starting_benches(self) -> None:
        for p in self.players:
            p.bench.new_bench()

    def fake_stage_one(self) -> None:
        for p in self.players:
            max_idx = len(Spl[2]) - 1
            random_agent1 = Spl[2][randint(0, max_idx)]
            random_agent2 = Spl[2][randint(0, max_idx)]
            random_agent3 = Spl[2][randint(0, max_idx)]
            p.bench.buy(random_agent1), p.bench.buy(random_agent2), p.bench.buy(random_agent3)
            p.gold += 10
            p.bench.print_bench(p.username)

    def set_stage(self) -> None:
        return

    def the_economy(self) -> None:
        return

    def end_of_round(self) -> None:
        return
