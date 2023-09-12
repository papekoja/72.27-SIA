import bisect
from itertools import accumulate

import math
import random

PROBABILISTIC_TOURNAMENT_VALUE = 0.75


def selection_method(population, selection_algorithm, selection_number, generation):
    if selection_algorithm == "elite":
        return elite_selection(population, selection_number)  # Return the result of elite selection
    elif selection_algorithm == "roulette":
        return roulette_selection(population, selection_number)
    elif selection_algorithm == "universal":
        return universal_selection(population, selection_number)
    elif selection_algorithm == "boltzmann":
        return boltzmann_selection(population, selection_number, generation)
    elif selection_algorithm == "determinist_tournament":
        return determinist_tournament_selection(population, selection_number)
    elif selection_algorithm == "probabilistic_tournament":
        return probabilistic_tournament_selection(population, selection_number)
    elif selection_algorithm == "rank":
        return rank_selection(population, selection_number)


def elite_selection(population, selection_number):
    population.sort(key=lambda x: x.get_fitness(), reverse=True)
    selected_population = []
    for index, individual in enumerate(population):
        n = math.ceil((selection_number - index) / len(population))
        for i in range(n):
            selected_population.append(individual)

    return selected_population


def roulette_selection(population, selection_number):
    selected_population = []
    total_fitness = sum(individual.get_fitness() for individual in population)
    relative_fitness = [individual.get_fitness() / total_fitness for individual in population]
    accumulated_fitness = list(accumulate(relative_fitness))
    random_numbers = [random.random() for _ in range(selection_number)]
    for number in random_numbers:
        index = bisect.bisect_left(accumulated_fitness,
                                   number)  # Find the index where number should be inserted in accumulated_fitness
        selected_population.append(population[index])

    return selected_population


def universal_selection(population, selection_number):
    selected_population = []
    total_fitness = sum(individual.get_fitness() for individual in population)
    relative_fitness = [individual.get_fitness() / total_fitness for individual in population]
    accumulated_fitness = list(accumulate(relative_fitness))
    random_number = random.random()
    numbers = [(random_number + i) / selection_number for i in range(selection_number)]
    for number in numbers:
        index = bisect.bisect_left(accumulated_fitness,
                                   number)  # Find the index where number should be inserted in accumulated_fitness
        selected_population.append(population[index])
    return selected_population


def boltzmann_selection(population, selection_number, generation):
    selected_population = []
    t0 = 1000
    tc = 500
    k = 2
    t = tc + (t0 - tc) * math.pow(math.e, -k * generation)
    num_population = len(population)
    average_pseudo_fitness = sum(
        math.pow(math.e, individual.get_fitness() / t) for individual in population) / num_population
    pseudo_fitness = [(math.pow(math.e, individual.get_fitness() / t) / average_pseudo_fitness) for individual in
                      population]
    total_pseudo_fitness = sum(pseudo_fitness)
    relative_pseudo_fitness = [value / total_pseudo_fitness for value in pseudo_fitness]
    accumulated_pseudo_fitness = list(accumulate(relative_pseudo_fitness))
    random_numbers = [random.random() for _ in range(selection_number)]
    for number in random_numbers:
        index = bisect.bisect_left(accumulated_pseudo_fitness,
                                   number)  # Find the index where number should be inserted in accumulated_fitness
        selected_population.append(population[index])
    return selected_population


def determinist_tournament_selection(population, selection_number):
    selected_population = []
    random.shuffle(population)
    m = 3
    while len(selected_population) < selection_number:
        sample = random.sample(population, m)
        sample.sort(key=lambda x: x.get_fitness(), reverse=True)
        selected_population.append(sample[0])
    return selected_population


def probabilistic_tournament_selection(population, selection_number):
    selected_population = []
    threshold = PROBABILISTIC_TOURNAMENT_VALUE
    while len(selected_population) < selection_number:
        selected_pair = random.sample(population, 2)  # Choose 2 individuals randomly
        r = random.random()
        if r < threshold:
            selected_individual = max(selected_pair, key=lambda x: x.get_fitness())
        else:
            selected_individual = min(selected_pair, key=lambda x: x.get_fitness())
        selected_population.append(selected_individual)
    return selected_population


def rank_selection(population, selection_number):
    selected_population = []
    population.sort(key=lambda x: x.get_fitness(), reverse=True)
    num_population = len(population)
    pseudo_fitness = [((num_population - rank) / num_population) for rank in range(1, num_population + 1)]
    total_pseudo_fitness = sum(pseudo_fitness)
    relative_pseudo_fitness = [value / total_pseudo_fitness for value in pseudo_fitness]
    accumulated_pseudo_fitness = list(accumulate(relative_pseudo_fitness))
    random_numbers = [random.random() for _ in range(selection_number)]
    for number in random_numbers:
        index = bisect.bisect_left(accumulated_pseudo_fitness,
                                   number)  # Find the index where number should be inserted in accumulated_fitness
        selected_population.append(population[index])
    return selected_population
