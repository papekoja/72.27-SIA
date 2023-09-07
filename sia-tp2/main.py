import configparser
import json
import numpy as np
from src.character import Character
from src.mutation_operators import mutate_population

# Load the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the parameters from the config file
amount_parents = int(config['GeneticAlgorithm']['population_number'])
number_iterations = int(config['GeneticAlgorithm']['max_generations'])
selection_method = str(config['GeneticAlgorithm']['selection_method'])

#result = genetic_algorithm(amount_parents, number_iterations, selection_method)