import math
import random
import copy
import numpy
import configparser

import numpy as np

from src.character import Character
from src.crossing_operators import crossing_operator
from src.mutation_operators import mutate_population
from src.replacement_methods import replacement_method
from src.selection_methods import selection_method


def genetic_algorithm(population_amount, character_type, selection_method1, selection_method2, selection_amount,
                      selection_probability, crossing_method, mutation_probability, multi_gen, uniform,
                      replacement_method1, replacement_method2, replacement_probability, number_iterations,
                      acceptable_solution, structure_percentage, by_content):
    population = []
    generation_tracker = []
    generation = 0
    selection_number1 = math.ceil(selection_amount * selection_probability)
    selection_number2 = selection_amount - selection_number1
    replacement_number1 = math.ceil(population_amount * replacement_probability)
    replacement_number2 = population_amount - replacement_number1

    # Generation 1
    for i in range(population_amount):
        s, a, e, r, h, height = random_stats_generator()
        population.append(Character(character_type, s, a, e, r, h, height))

    generation_tracker.append(
        {"max_fitness": max(population, key=lambda x: x.get_fitness()).get_fitness(), "population": population})

    # Generation 2 to n
    while check_end_condition(generation_tracker, generation, number_iterations, acceptable_solution,
                              structure_percentage, by_content):
        generation += 1
        children = []

        # SELECTION
        selected_population1 = selection_method(population, selection_method1, selection_number1, generation)
        selected_population2 = selection_method(population, selection_method2, selection_number2, generation)
        selected_population = selected_population1 + selected_population2

        # CROSSING
        for i, j in zip(range(0, selection_amount, 2), range(1, selection_amount, 2)):
            parent1 = selected_population[i]
            parent2 = selected_population[j]
            ch1, ch2, = crossing_operator(parent1, parent2, crossing_method)
            children.append(ch1)
            children.append(ch2)

        # MUTATION
        mutate_population(children, mutation_probability, multi_gen)
        mutation_probability *= 1 if uniform else 0.9

        # REPLACEMENT
        new_population1 = replacement_method(population, replacement_method1, children)
        new_population1 = random.sample(new_population1, replacement_number1)
        new_population2 = replacement_method(population, replacement_method2, children)
        new_population2 = random.sample(new_population2, replacement_number2)
        population = new_population1 + new_population2

        generation_tracker.append(
            {"max_fitness": max(population, key=lambda x: x.get_fitness()).get_fitness(), "population": population})

    for gen in generation_tracker:
        print(gen["max_fitness"])


def random_stats_generator():
    while True:
        strength = random.randint(1, 100)
        agility = random.randint(1, 100)
        expertise = random.randint(1, 100)
        resistance = random.randint(1, 100)
        health = random.randint(1, 100)

        # Calculate the sum of attributes
        total = strength + agility + expertise + resistance + health

        # Check if the sum is equal to 150
        if total == 150:
            break  # Exit the loop if the constraint is met
    height = random.uniform(1.3, 2.0)

    return strength, agility, expertise, resistance, health, height


def check_end_condition(generation_tracker, generation, number_iterations, acceptable_solution, structure_percentage,
                        by_content):
    if acceptable_solution > 0:
        last_generation = generation_tracker[generation]
        return last_generation["max_fitness"] < acceptable_solution
    elif structure_percentage > 0:
        if generation < number_iterations:
            return True
        last_generations = generation_tracker[-number_iterations:]
        last_populations = [last_generation["population"] for last_generation in last_generations]
        for last_population in last_populations:
            last_population.sort(key=lambda x: x.get_fitness(), reverse=True)
        relevant_number = math.ceil(len(last_populations[0]) * structure_percentage)
        relevant_populations = [last_population[:relevant_number] for last_population in last_populations]
        for i in range(1, number_iterations):
            for j in range(relevant_number):
                if relevant_populations[0][j].get_fitness() != relevant_populations[i][j].get_fitness():
                    return True
        return False
    elif by_content:
        if generation < number_iterations:
            return True
        last_generations = generation_tracker[-number_iterations:]
        first_fitness = last_generations[0]["max_fitness"]
        return not all(gen["max_fitness"] == first_fitness for gen in last_generations)
    elif number_iterations is not None:
        return generation < number_iterations
    return False

# Se generan dos hijos por pareja, de ellos se toma uno random
# De la poblacion vieja se toma la mitad tambien
# def genetic_algorithm(population, best_caracter_founded, selection_algorithm, mutation_rate, max_generations, expected_fitness,population_size,fitness_cut):
#     expected_fitness = validation_fitness(expected_fitness)
#     closest_fit = 0
#     generation_maxes = []
#     gen = 0
#     populations=[]
#     while gen < (limit_generation):
#         max=None
#         populations.append(copy.deepcopy(population))
#         parents = copy.deepcopy(population)
#         selection_method(parents, best_caracter_founded, selection_algorithm)
#         n = len(parents)
#         random.shuffle(parents)
#         if n % 2 == 1:
#             parents.append(copy.deepcopy(parents[0]))
#         child_pop=[]
#         for i in range(0, n, 2):
#             child1,child2 = uniform_crossbreed(parents[i],parents[i+1])
#             child_pop.append(child1)
#             child_pop.append(child2)

#         # nos quedamos con los mejores de la vieja poblacion 
#         # Mutamos de forma uniforme a la antigua generacion 
#         uniform_mutation(child_pop,mutation_rate)

#         new_pop = []
#         new_pop.extend(child_pop)

#         i = 0
#         while len(new_pop) < population_size and i < len(parents):
#            new_pop.append(parents[i])

#         max = new_pop[0]
#         for individual in new_pop:
#             if individual.get_fitness(best_caracter_founded) > max.get_fitness(best_caracter_founded):
#                 max = EachColor(individual.red, individual.green, individual.blue,mutation_rate)
#         generation_maxes.append(max.get_fitness(best_caracter_founded))

#         if(fitness_cut and max.get_fitness(best_caracter_founded) >= expected_fitness):
#             print("Encontrado en la generacion numero: " + str(gen))
#             return max,generation_maxes,populations


#         population = new_pop
#         gen += 1
#         if not fitness_cut and gen >= max_generations:
#             return max, generation_maxes, populations

#     return max, generation_maxes, populations
