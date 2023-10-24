from TheGame import Game


def all_players_stage1_benches_gold():
    game1 = Game()
    game1.make_players()
    game1.make_starting_benches()
    game1.fake_stage_one()
    for player in game1.players:
        player.bench.print_bench(player.username)
        print(f"{player.username} has {player.gold} gold.")


def stage_one_field():
    game2 = Game()
    game2.make_players()
    game2.make_starting_benches()
    game2.fake_stage_one()
    counter = 0
    for player in game2.players:
        if counter == 2:
            break
        player.bench_to_field()
        player.field.list_agents()
        player.field.total_power()
        counter += 1


if __name__ == '__main__':
    test = input("What test #?: ")
    if test == str(1):
        all_players_stage1_benches_gold()
    if test == str(2):
        stage_one_field()
