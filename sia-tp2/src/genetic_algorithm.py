import math
import random
import copy
import numpy

from src.character import Character
from src.crossing_operators import one_point_crossing
from src.selection_methods import selection_method



def genetic_algorithm(number_parents, number_iterations):
    fitness_dict = {}
    
    # Gen 1
    # This creates an n amount of characters defined in main.py. This is only for the first generation

    # TODO - store the enire character object in the dictionary
    for i in range(number_parents):
        s, a, e, r, h, height = random_stats_generator()
        character = Character('warrior', s, a, e, r, h, height)
        fitness_dict[i] = character.gene1
    

    # TODO - avg fitness doesn't work because i haven't stored the entire character object in the dictionary.
    # avg = avg_fitness(fitness_dict)
    print(character.gene1)

    population = {1:1, 2:2, 3:3, 4:4, 5:5}
    # selection method
    selection_method(population, )




    # Gen 2 (for now because number_iterations = 2)
    p1 = 1
    p2 = 2
    for i in range(number_iterations - 1):
        one_point_crossing(p1, p2, False, False)
        
        character_v2 = Character('warrior', None, None, None, None, None, None, character.gene1, character.gene2)

    print(avg)






def avg_fitness(fitness_dict):
    total_fitness = sum(fitness_dict.values())  # Sum of all fitness values
    num_characters = len(fitness_dict)          # Number of characters in the dictionary
    average_fitness = total_fitness / num_characters
    
    return average_fitness


# TODO Change this method in a cleaner way...
# I know this is a bit of a random bruteforce way of doing it. Might change this later
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