import numpy as np


def replacement_method(population, replacement_algorithm, children):
    if replacement_algorithm == "traditional":
        return traditional_replacement(population, children)
    elif replacement_algorithm == "young":
        return young_replacement(population, children)


def traditional_replacement(population, children):
    everyone = population + children
    return np.random.choice(everyone, len(population))


def young_replacement(population, children):
    if len(children) > len(population):
        return np.random.choice(children, len(population))
    return children + np.random.choice(population, len(population) - len(children))
