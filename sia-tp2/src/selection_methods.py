import bisect
from itertools import accumulate

import numpy as np
import math
import copy
import random
from src.character import Character

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

    # population.sort(key=lambda x: x['fitness'], reverse=True)
    # num_to_select = math.ceil(len(population) / 2)
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

    # total_fitness = sum(individual.get_fitness() for individual in population)
    # relative_fitness = [individual.get_fitness() / total_fitness for individual in population]
    # selection_probabilities = [individual.get_fitness() / total_fitness for individual in population]
    # selected_individuals = np.random.choice(population, size=len(population)//2, replace=True, p=selection_probabilities)
    # return selected_individuals.tolist()


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

    # population.sort(key=lambda x: x.get_fitness())
    # num_individuals = len(population)
    # selection_probabilities = [individual.get_fitness() for individual in population]
    # total_fitness = sum(selection_probabilities)
    # normalized_probabilities = [prob / total_fitness for prob in selection_probabilities]
    # num_spins = num_individuals // 2
    # selected_individuals = []
    # pointer = random.uniform(0, 1 / num_spins)
    # for _ in range(num_spins):
    #     while pointer > normalized_probabilities[0]:
    #         pointer -= normalized_probabilities[0]
    #         normalized_probabilities.pop(0)
    #         population.pop(0)
    #     selected_individuals.append(population[0])
    #     pointer += 1 / num_spins
    # return selected_individual


def boltzmann_selection(population, selection_number, generation):  # TODO see what to do with t0, tc and k
    selected_population = []
    t0 = 1000
    tc = 500
    k = 1
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

    # fitness_values = [individual.get_fitness() for individual in population]
    # scaled_fitness = np.array(fitness_values) / temperature
    # exponentials = np.exp(scaled_fitness)
    # probabilities = exponentials / np.sum(exponentials)
    # selected_individuals = np.random.choice(population, size=len(population)//2, replace=True, p=probabilities)
    # return selected_individuals.tolist()


def determinist_tournament_selection(population, selection_number):
    selected_population = []
    random.shuffle(population)
    m = 3
    while len(selected_population) < selection_number:
        sample = random.sample(population, m)
        sample.sort(key=lambda x: x.get_fitness(), reverse=True)
        selected_population.append(sample[0])
    return selected_population

    # random.shuffle(population)
    # selected_population = []
    # k = math.ceil(len(population)/2)
    # while len(selected_population) < k:
    #     sample = np.random.choice(population, size=len(population)//3)
    #     sample.sort(key=lambda x: x.get_fitness(), reverse=True)
    #     selected_population.append(copy.deepcopy(sample[0]))
    # return selected_population


def probabilistic_tournament_selection(population, selection_number):
    selected_population = []
    threshold = PROBABILISTIC_TOURNAMENT_VALUE  # TODO see what to do with this
    while len(selected_population) < selection_number:
        selected_pair = random.sample(population, 2)  # Choose 2 individuals randomly
        r = random.random()
        if r < threshold:
            selected_individual = max(selected_pair, key=lambda x: x.get_fitness())
        else:
            selected_individual = min(selected_pair, key=lambda x: x.get_fitness())
        selected_population.append(selected_individual)
    return selected_population

    # selected_individuals = []
    # threshold_range = (0.5, 1.0)
    # while len(selected_individuals) < selection_number:
    #     selected_pair = random.sample(population, 2)  # Choose 2 individuals randomly
    #     r = random.uniform(0, 1)
    #     threshold = random.uniform(*threshold_range)  # Random threshold value in the specified range
    #     if r < threshold:
    #         selected_individual = max(selected_pair, key=lambda x: x.get_fitness())
    #     else:
    #         selected_individual = min(selected_pair, key=lambda x: x.get_fitness())
    #     selected_individuals.append(copy.deepcopy(selected_individual))
    # return selected_individuals


def rank_selection(population, selection_number):
    selected_population = []
    population.sort(key=lambda x: x.get_fitness())
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

    # population.sort(key=lambda x: x.get_fitness())
    # num_individuals = len(population)
    # selection_probabilities = [((num_individuals - rank) / (num_individuals * (num_individuals + 1) / 2)) for rank in range(1, num_individuals + 1)]
    # selected_individuals = random.choices(population, weights=selection_probabilities, k=num_individuals // 2)
    # return selected_individuals
