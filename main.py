from TheGame import Game


def main():
    game1 = Game()
    game1.make_players()
    game1.make_starting_benches()
    game1.fake_stage_one()

if __name__ == '__main__':
    main()
