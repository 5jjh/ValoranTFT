from Agents import Agent
from AgentLists import all_agents
# SLL Data Structure


class NewSlot:
    def __init__(self, agent=Agent, next=None) -> None:
        self.agent = Agent
        self.next = next


class TheList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def empty(self) -> bool:
        if self.head is None:
            return True
        return False

    def append(self, agent=Agent) -> None:
        new_agent = NewSlot(agent)
        if self.empty():
            self.head = self.tail = new_agent
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = self.tail = new_agent

    def remove(self, agent: Agent in all_agents) -> None:
        curr = self.head
        if self.empty():
            return
        elif self.head.agent == agent:
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            while curr.next is not None:
                if curr.next.agent == agent:
                    if curr.next is self.tail:
                        curr.next = None
                        self.tail = curr
                        return
                    curr.next = curr.next.next
                    return
                curr = curr.next

    def pop(self) -> None:
        if self.empty():
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
