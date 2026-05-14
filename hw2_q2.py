from enum import Enum
from collections import namedtuple
from itertools import islice

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def worsen(condition):

    if condition == Condition.SICK:
        return Condition.DYING

    if condition == Condition.DYING:
        return Condition.DEAD

    return condition

def improve(condition):

    if condition == Condition.DYING:
        return Condition.SICK

    if condition == Condition.SICK:
        return Condition.HEALTHY

    return condition

def meet(a1, a2):

    c1, c2 = a1.category, a2.category


    # Cure improves the other agent (apart from cure)
    if c1 == Condition.CURE and c2 != Condition.CURE:
        return [a1, Agent(a2.name, improve(c2))]
    if c2 == Condition.CURE and c1 != Condition.CURE:
        return [Agent(a1.name, improve(c1)), a2]
    if c1 == Condition.CURE and c2 == Condition.CURE:
        return [a1, a2]

    # Otherwise both worsen
    return [
        Agent(a1.name, worsen(c1)),
        Agent(a2.name, worsen(c2))
    ]

def meetup(agent_listing: tuple) -> list:
    active_agents = [a for a in agent_listing if a.category not in (Condition.HEALTHY, Condition.DEAD)]
    inactive_agents = [a for a in agent_listing if a.category in (Condition.HEALTHY, Condition.DEAD)]

    result = []
    it = iter(active_agents)

    while True:
        pair = list(islice(it, 2))
        if not pair:
            break
        if len(pair) == 2:
            result.extend(meet(pair[0], pair[1]))
        else:
            result.append(pair[0])

    return result + inactive_agents

if __name__ == "__main__":
    pass