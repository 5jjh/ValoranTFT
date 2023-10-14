from TheSLL import TheList
from StoresPerLevel import StoreAndLevel as Spl
from random import randint
from Agents import Agent
# SLL that represents the player's store.


class BoughtAgent(Agent):
    name = "Already bought!"
    role = tier = level = None


class Store(TheList):
    def new_store(self, player_level) -> None:
        counter = 0
        while counter < 5:
            max_idx = len(Spl[player_level]) - 1
            the_agent = Spl[player_level][randint(0, max_idx)]
            self.append(the_agent)
            counter += 1

    def print_store(self) -> None:
        curr = self.head
        counter = 1
        print(f"The Store:")
        while curr is not None:
            if curr.agent is BoughtAgent:
                print(f"{counter}: {curr.agent.name}")
            else:
                print(f"{counter}: {curr.agent.name} (Cost = {curr.agent.tier})")
            counter += 1
            curr = curr.next

    def clear_store(self) -> None:
        while self.empty() is False:
            self.pop()

    def bought_agent(self, agent) -> None:
        the_agent = 1
        curr = self.head
        while the_agent != agent:
            the_agent += 1
            curr = curr.next
        print(f"You bought {curr.agent.name} for {curr.agent.tier} gold!")
        curr.agent = BoughtAgent
        self.print_store()
