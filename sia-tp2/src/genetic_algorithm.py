import math
import random
import copy
import numpy
import configparser

from src.character import Character
from src.crossing_operators import one_point_crossing
from src.selection_methods import selection_method, elite_selection

config = configparser.ConfigParser()
config.read('config.ini')
character_type = str(config['GeneticAlgorithm']['character_type'])

def genetic_algorithm(number_parents, number_iterations, method):
    population = []
    generation_tracker = {}
    generation = 0
    sum = 0
    
    # Generation 1
    for i in range(number_parents):             # Create i amount of characters in population
        s, a, e, r, h, height = random_stats_generator()
        population.append(Character(character_type, s, a, e, r, h, height))
        sum += population[i].get_fitness()

    avg_fitness = sum / len(population)
    generation_tracker[generation] = avg_fitness


    # Generation 2 to n
    for i in range(number_iterations):
        selection_algorigthm = method
        population = selection_method(population, selection_algorigthm)
        population = population + population  
        
        dummy = 0
        for j in range(len(population)):
            dummy += population[j].get_fitness()
        total = dummy / len(population)

        generation_tracker[generation[i]] = total

        # Get population fitness
        # # total = sum(population[j].get_fitness() for j in range(len(population)))
        # print(total)
        # avg_fitness = total / len(population)
        # print(avg_fitness)

        # TODO - Cross
        # ch1, ch2, = one_point_crossing(character_dict, character_dict, True, True)


        # TODO - Mutate

        # avg_fitness = sum(character_dict['fitness'] for character_dict in population) / len(population)
        
        # generation_tracker[generation] = avg_fitness

    print(generation_tracker)








def avg_fitness(fitness_dict):
    total_fitness = sum(fitness_dict.values())  # Sum of all fitness values
    num_characters = len(fitness_dict)          # Number of characters in the dictionary
    average_fitness = total_fitness / num_characters
    
    return average_fitness



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

        
        
        # TODO - this is if we fix the int-float item problem

        # # Generate five random floats between 0 and 100
        # strength = random.uniform(0, 100)
        # agility = random.uniform(0, 100)
        # expertise = random.uniform(0, 100)
        # resistance = random.uniform(0, 100)
        # health = random.uniform(0, 100)

        # # Calculate the sum of the five attributes
        # total = strength + agility + expertise + resistance + health

        # # Adjust the values to ensure the sum is 150
        # scaling_factor = 150 / total
        # strength *= scaling_factor
        # agility *= scaling_factor
        # expertise *= scaling_factor
        # resistance *= scaling_factor
        # health *= scaling_factor

    # Generate a random height within the specified range
    height = random.uniform(1.3, 2.0)

    return strength, agility, expertise, resistance, health, height





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