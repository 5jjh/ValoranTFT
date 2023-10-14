# Keeps track of the player's gold, level, and HP

class Player(object):
    def __init__(self, username, gold=0, level=1, hp=100):
        self.username = input("Welcome to ValoranTFT! Input your username: ")
        self.gold = gold
        self.level = level
        self.hp = hp
