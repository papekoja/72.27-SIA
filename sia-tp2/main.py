import configparser
import json
import numpy as np
from src.character import Character
from src.mutation_operators import mutate_population


from src.genetic_algorithm import genetic_algorithm

number_parents = 100
number_iterations = 2
selection_method = 'elite'

result = genetic_algorithm(number_parents, number_iterations, selection_method)

character = Character("warrior", 30, 30, 30, 30, 30, 1.6)
print(character)
mutate_population([character], 20, False)
print(character)