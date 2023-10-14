# Creating agent objects.

class Agent(object):
    def __init__(self, name, role, tier, level):
        self.name = name
        self.role = role
        self.tier = tier
        self.level = level


class Brimstone(Agent):
    name = "Brimstone"
    role = "C"
    tier = 2
    level = 1


class Astra(Agent):
    name = "Astra"
    role = "C"
    tier = 3
    level = 1


class Harbor(Agent):
    name = "Harbor"
    role = "C"
    tier = 1
    level = 1


class Viper(Agent):
    name = "Astra"
    role = "C"
    tier = 4
    level = 1


class Omen(Agent):
    name = "Omen"
    role = "C"
    tier = 5
    level = 1


class Sova(Agent):
    name = "Sova"
    role = "I"
    tier = 5
    level = 1


class Skye(Agent):
    name = "Skye"
    role = "I"
    tier = 4
    level = 1


class Breach(Agent):
    name = "Breach"
    role = "I"
    tier = 3
    level = 1


class Kayo(Agent):
    name = "KAY/O"
    role = "I"
    tier = 3
    level = 1


class Gekko(Agent):
    name = "Gekko"
    role = "I"
    tier = 1
    level = 1


class Fade(Agent):
    name = "Fade"
    role = "I"
    tier = 2
    level = 1


class Jett(Agent):
    name = "Jett"
    role = "D"
    tier = 4
    level = 1


class Raze(Agent):
    name = "Raze"
    role = "D"
    tier = 5
    level = 1


class Yoru(Agent):
    name = "Yoru"
    role = "D"
    tier = 2
    level = 1


class Reyna(Agent):
    name = "Reyna"
    role = "D"
    tier = 3
    level = 1


class Phoenix(Agent):
    name = "Phoenix"
    role = "D"
    tier = 2
    level = 1


class Neon(Agent):
    name = "Neon"
    role = "D"
    tier = 1
    level = 1


class Cypher(Agent):
    name = "Cypher"
    role = "S"
    tier = 4
    level = 1


class Killjoy(Agent):
    name = "Killjoy"
    role = "S"
    tier = 5
    level = 1


class Deadlock(Agent):
    name = "Deadlock"
    role = "S"
    tier = 1
    level = 1


class Sage(Agent):
    name = "Sage"
    role = "S"
    tier = 3
    level = 1


class Chamber(Agent):
    name = "Chamber"
    role = "S"
    tier = 2
    level = 1
