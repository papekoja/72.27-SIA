import numpy as np
import math
import copy
import random
from character import Character

PROBABILISTIC_TOURNAMENT_VALUE = 0.75

def selection_method(population, selection_algorithm):
    if selection_algorithm == "elite":
        elite_selection(population)
    elif selection_algorithm == "roulette":
        roulette_selection(population)
    elif selection_algorithm == "universal":
        universal_selection(population)
    elif selection_algorithm == "boltzmann":
        boltzmann_selection(population)
    elif selection_algorithm=="determinist_tournament":
         determinist_tournament_selection(population)
    elif selection_algorithm=="probabilistic_tournament":
         probabilistic_tournament_selection(population)
    elif selection_algorithm == "rank":
        rank_selection(population)


def elite_selection(population):
    population.sort(key=lambda x: x.get_fitness(), reverse=True)
    return population[0:math.ceil(len(population)/2)]

def roulette_selection(population):
    total_fitness = sum(individual.get_fitness() for individual in population)
    selection_probabilities = [individual.get_fitness() / total_fitness for individual in population]
    selected_individuals = np.random.choice(population, size=len(population)//2, replace=True, p=selection_probabilities) 
    return selected_individuals.tolist()

def universal_selection(population):
    population.sort(key=lambda x: x.get_fitness())
    num_individuals = len(population)
    selection_probabilities = [individual.get_fitness() for individual in population]
    total_fitness = sum(selection_probabilities)
    normalized_probabilities = [prob / total_fitness for prob in selection_probabilities]
    num_spins = num_individuals // 2
    selected_individuals = []
    pointer = random.uniform(0, 1 / num_spins)
    for _ in range(num_spins):
        while pointer > normalized_probabilities[0]:
            pointer -= normalized_probabilities[0]
            normalized_probabilities.pop(0)
            population.pop(0)
        selected_individuals.append(population[0])
        pointer += 1 / num_spins
    return selected_individuals

def boltzmann_selection(population, temperature):   # TO CHECK
    fitness_values = [individual.get_fitness() for individual in population]
    scaled_fitness = np.array(fitness_values) / temperature
    exponentials = np.exp(scaled_fitness)
    probabilities = exponentials / np.sum(exponentials)
    selected_individuals = np.random.choice(population, size=len(population)//2, replace=True, p=probabilities)
    return selected_individuals.tolist()

    
def determinist_tournament_selection(population):
    random.shuffle(population)
    population_selected = []
    K = math.ceil(len(population)/2)
    while len(population_selected) < K:
        sample = np.random.choice(population, size=len(population)//3)
        sample.sort(key=lambda x: x.get_fitness(), reverse=True)
        population_selected.append(copy.deepcopy(sample[0]))
    return population_selected

def probabilistic_tournament_selection(population):
    selected_individuals = []
    threshold_range = (0.5, 1.0)
    K = math.ceil(len(population)/2)
    while len(selected_individuals) < K:
        selected_pair = random.sample(population, 2)  # Choose 2 individuals randomly
        r = random.uniform(0, 1)
        threshold = random.uniform(*threshold_range)  # Random threshold value in the specified range
        if r < threshold:
            selected_individual = max(selected_pair, key=lambda x: x.get_fitness())
        else:
            selected_individual = min(selected_pair, key=lambda x: x.get_fitness())
        selected_individuals.append(copy.deepcopy(selected_individual))
    return selected_individuals

def rank_selection(population):
    population.sort(key=lambda x: x.get_fitness())
    num_individuals = len(population)
    selection_probabilities = [((num_individuals - rank) / (num_individuals * (num_individuals + 1) / 2)) for rank in range(1, num_individuals + 1)]
    selected_individuals = random.choices(population, weights=selection_probabilities, k=num_individuals // 2)
    return selected_individuals

