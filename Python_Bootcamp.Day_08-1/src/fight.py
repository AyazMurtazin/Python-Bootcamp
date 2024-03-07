import asyncio

from enum import Enum, auto
from random import choice


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)


async def fight():
    countermeasures = {Action.HIGHBLOCK: (Action.LOWKICK, 1),
                       Action.LOWBLOCK: (Action.HIGHKICK, 1),
                       Action.HIGHKICK: (Action.HIGHBLOCK, 0),
                       Action.LOWKICK: (Action.LOWBLOCK, 0)}
    agent = Agent()
    async for agent_move in agent:
        neo_move, damage = countermeasures[agent_move]
        agent.health -= damage
        print(
            f"Agent: {agent_move}, Neo: {neo_move}, Agent Health: {agent.health}")
        if agent.health <= 0:
            break
    print("Neo wins!")


if __name__ == "__main__":
    asyncio.run(fight())
