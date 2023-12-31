from TheField import Field
from TheBench import Bench, EmptySlot
from TheStore import Store
# Keeps track of the player's gold, level, and HP


class Player(object):
    def __init__(self, username=input("Welcome to ValoranTFT! Input your username: "), gold=0, level=1, hp=100) -> None:
        self.username = username
        self.gold = gold
        self.level = level
        self.hp = hp
        self.field = Field()
        self.bench = Bench()
        self.store = Store()
        self.result = None
        self.past_result = None
        self.streak = 0

    def increase_level(self) -> None:
        self.level += 1

    def battle_result(self) -> None:
        battle = 1
        if battle:
            self.result = True
        else:
            self.result = False
        return

    def result_streak(self) -> int:
        counter = 1
        if self.result and self.past_result:
            counter += 1
        elif not self.result and not self.past_result:
            counter += 1
        else:
            counter = 1
        self.past_result = self.result
        return counter

    def bench_to_field(self) -> None:
        curr = self.bench.head
        while curr is not None:
            if curr.agent is EmptySlot:
                curr = curr.next
            else:
                ans = input(f"Would you like to move: {curr.agent.name} with power {curr.agent.level * curr.agent.tier}"
                            f" to your field?")
                if ans.lower() == 'y':
                    self.field.add_agent(curr)
                    self.bench.remove(curr)
                    curr = curr.next
                elif ans.lower() == 'n':
                    curr = curr.next
                else:
                    print(f"Not a valid input. Please enter 'Y' or 'N'")
