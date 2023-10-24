from TheSLL import TheList
from Agents import Agent
from StoresPerLevel import *
from random import randint
from AgentLists import all_agents


# SLL that represents the player's bench.


class EmptySlot(Agent):
    name = "Empty"
    role = tier = level = None


class Bench(TheList):
    def new_bench(self) -> None:
        max_idx = len(level_1_store) - 1
        the_agent = level_1_store[randint(0, max_idx)]
        self.append(the_agent)

    def print_bench(self, username) -> None:
        curr = self.head
        counter = 1
        print(f"{username}'s Bench:")
        result = ""
        while curr is not None:
            if curr.agent is EmptySlot:
                result += curr.agent.name
            elif curr is self.tail:
                result += f"{counter}: {curr.agent.name} (Level = {curr.agent.level})"
            else:
                result += f"{counter}: {curr.agent.name} (Level = {curr.agent.level}) "
            counter += 1
            curr = curr.next
        print(result)

    def buy(self, agent: Agent in all_agents) -> None:
        self.append(agent)

    def sell(self, agent: Agent in all_agents) -> None:
        self.remove(agent)
