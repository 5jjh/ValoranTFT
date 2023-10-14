from Agents import Agent
from TheBench import Bench

# A player's field in which they place their agents from their bench
# A dictionary that holds the agent name as the key and the overall power of the agent (tier * level) as the value.


class Field(object):
    def __init__(self):
        self.field = {}

    def list_agents(self) -> str:
        result = ""
        for agent in self.field.keys():
            result += f"Agent: {agent.name} Power: {self.field[agent]}.'\n'"
        return result

    def add_agent(self, agent: Agent) -> None:
        if agent.name in self.field.keys():
            agent.name = agent.name + ' 2'
        self.field[agent.name] = agent.tier * agent.level

    def remove_agent(self, agent: Agent) -> None:
        del self.field[agent.name]
        doubled_agent = agent.name + ' 2'
        if doubled_agent in self.field.keys():
            self.field[agent.name] = self.field[doubled_agent]
            del self.field[doubled_agent]
        return
