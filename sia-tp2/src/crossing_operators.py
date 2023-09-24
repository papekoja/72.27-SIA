import math
import random
from src.character import Character

ITEM_NUMBER = 15000


def crossing_operator(parent1, parent2, crossing_algorithm):
    if crossing_algorithm == "one_point":
        return one_point_crossing(parent1, parent2)
    elif crossing_algorithm == "two_point":
        return two_point_crossing(parent1, parent2)
    elif crossing_algorithm == "uniform":
        return uniform_crossing(parent1, parent2)
    elif crossing_algorithm == "anular":
        return anular_crossing(parent1, parent2)


def one_point_crossing(parent1, parent2):
    # GENE 1
    p = random.randint(0, ITEM_NUMBER)
    child1_new_gene1 = parent1.gene1[0:p] + parent2.gene1[p:]
    child2_new_gene1 = parent2.gene1[0:p] + parent1.gene1[p:]
    # GENE 2
    p = random.randint(0, 5)
    child1_new_gene2 = parent1.gene2[0:p] + parent2.gene2[p:]
    child2_new_gene2 = parent2.gene2[0:p] + parent1.gene2[p:]

    child1 = Character(parent1.type, None, None, None, None, None, None, child1_new_gene1, child1_new_gene2)
    child2 = Character(parent1.type, None, None, None, None, None, None, child2_new_gene1, child2_new_gene2)
    return child1, child2


def two_point_crossing(parent1, parent2):
    # GENE 1
    p1 = random.randint(0, ITEM_NUMBER)
    p2 = random.randint(p1, ITEM_NUMBER)  # Ensure p2 is greater than p1
    child1_new_gene1 = parent1.gene1[0:p1] + parent2.gene1[p1:p2] + parent1.gene1[p2:]
    child2_new_gene1 = parent2.gene1[0:p1] + parent1.gene1[p1:p2] + parent2.gene1[p2:]
    # GENE 2
    p1 = random.randint(0, 5)
    p2 = random.randint(p1, 5)  # Ensure p2 is greater than p1
    child1_new_gene2 = parent1.gene2[0:p1] + parent2.gene2[p1:p2] + parent1.gene2[p2:]
    child2_new_gene2 = parent2.gene2[0:p1] + parent1.gene2[p1:p2] + parent2.gene2[p2:]

    child1 = Character(parent1.type, None, None, None, None, None, None, child1_new_gene1, child1_new_gene2)
    child2 = Character(parent1.type, None, None, None, None, None, None, child2_new_gene1, child2_new_gene2)

    return child1, child2


def uniform_crossing(parent1, parent2):
    child1_new_gene1 = []
    child2_new_gene1 = []
    child1_new_gene2 = []
    child2_new_gene2 = []

    # GENE 1
    for i in range(ITEM_NUMBER):
        if random.random() > 0.5:
            child1_new_gene1.append(parent1.gene1[i])
            child2_new_gene1.append(parent2.gene1[i])
        else:
            child1_new_gene1.append(parent2.gene1[i])
            child2_new_gene1.append(parent1.gene1[i])
    if len(child1_new_gene1) + len(child1_new_gene1) != (ITEM_NUMBER * 2):
        raise RuntimeError("Problem in uniform_crossbreed gene1")
    # GENE 2
    for i in range(6):
        if random.random() > 0.5:
            child1_new_gene2.append(parent1.gene2[i])
            child2_new_gene2.append(parent2.gene2[i])
        else:
            child1_new_gene2.append(parent2.gene2[i])
            child2_new_gene2.append(parent1.gene2[i])
    if len(child1_new_gene2) + len(child1_new_gene2) != 12:
        raise RuntimeError("Problem in uniform_crossbreed gene2")

    child1 = Character(parent1.type, None, None, None, None, None, None, child1_new_gene1, child1_new_gene2)
    child2 = Character(parent1.type, None, None, None, None, None, None, child2_new_gene1, child2_new_gene2)

    return child1, child2


def anular_crossing(parent1, parent2):
    # GENE 1
    p1 = random.randint(0, ITEM_NUMBER - 1)
    l = random.randint(0, math.ceil(ITEM_NUMBER / 2))
    p2 = (p1 + l) % ITEM_NUMBER
    if p1 > p2:
        p1, p2 = p2, p1
    child1_new_gene1 = parent1.gene1[0:p1] + parent2.gene1[p1:p2] + parent1.gene1[p2:]
    child2_new_gene1 = parent2.gene1[0:p1] + parent1.gene1[p1:p2] + parent2.gene1[p2:]
    # GENE 2
    p1 = random.randint(0, 5)
    l = random.randint(0, 3)
    p2 = (p1 + l) % 6
    if p1 > p2:
        p1, p2 = p2, p1
    child1_new_gene2 = parent1.gene2[0:p1] + parent2.gene2[p1:p2] + parent1.gene2[p2:]
    child2_new_gene2 = parent2.gene2[0:p1] + parent1.gene2[p1:p2] + parent2.gene2[p2:]

    child1 = Character(parent1.type, None, None, None, None, None, None, child1_new_gene1, child1_new_gene2)
    child2 = Character(parent1.type, None, None, None, None, None, None, child2_new_gene1, child2_new_gene2)

    return child1, child2
