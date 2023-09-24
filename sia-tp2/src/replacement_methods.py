import random


def replacement_method(population, replacement_algorithm, children):
    if replacement_algorithm == "traditional":
        return traditional_replacement(population, children)
    elif replacement_algorithm == "young":
        return young_replacement(population, children)


def traditional_replacement(population, children):
    everyone = population + children
    return random.sample(everyone, len(population))


def young_replacement(population, children):
    if len(children) > len(population):
        return random.sample(children, len(population))
    return children + random.sample(population, len(population) - len(children))
