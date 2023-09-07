import math
import random
import copy
import numpy
import configparser

from src.character import Character
from src.crossing_operators import crossing_operator
from src.selection_methods import selection_method, elite_selection

config = configparser.ConfigParser()
config.read('config.ini')
character_type = str(config['GeneticAlgorithm']['character_type'])

def genetic_algorithm(number_parents, number_iterations, method):
    population = []
    generation_tracker = {}
    generation = 0
    total_sum = 0
    
    # Generation 1
    for i in range(number_parents):
        s, a, e, r, h, height = random_stats_generator()
        population.append(Character(character_type, s, a, e, r, h, height))
        total_sum += population[i].get_fitness()

    avg_fitness = total_sum / len(population)
    generation_tracker[generation] = avg_fitness


    # Generation 2 to n
    # Here, implement the selection method.
    for generation in range(1, number_iterations + 1):
        population = selection_method(population, method)
        population += population                    # TODO - Now it assumes a 50 50 split. In te config.ini, a percentage is stated. Maybe look at this later on.

        total_fitness = sum(character.get_fitness() for character in population)
        avg_fitness = total_fitness / len(population)


        # TODO - Cross - This doesn't seem to affect anything yet....
        for i, j in zip(range(0, len(population), 2), range(1, len(population), 2)):
            ch1_parrent = population[i]
            ch2_parrent = population[j]
            ch1, ch2, = crossing_operator(ch1_parrent, ch2_parrent, True, False, "one_point")

            # TODO - place the ch1 and ch2 in the population so that it replaces the entire old population
            # population[i] = ch1
            # population[j] = ch2


        # TODO - Mutate
        

        generation_tracker[generation] = avg_fitness

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