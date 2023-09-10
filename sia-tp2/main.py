import configparser
import json
import numpy as np
from src.character import Character
from src.mutation_operators import mutate_population

from src.genetic_algorithm import genetic_algorithm

# Load the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the parameters from the config file
population_amount = int(config['Population']['population_amount'])
character_type = str(config['Population']['character_type'])

selection_method1 = str(config['Selection']['selection_method1'])
selection_method2 = str(config['Selection']['selection_method2'])
selection_amount = int(config['Selection']['selection_amount'])
selection_probability = float(config['Selection']['selection_probability'])

crossing_method = str(config['Crossing']['crossing_method'])

mutation_probability = float(config['Mutation']['mutation_probability'])
multi_gen = config.getboolean('Mutation', 'multi_gen')
uniform = config.getboolean('Mutation', 'uniform')

replacement_method1 = str(config['Replacement']['replacement_method1'])
replacement_method2 = str(config['Replacement']['replacement_method2'])
replacement_probability = float(config['Replacement']['replacement_probability'])

number_iterations = int(config['EndCondition']['number_iterations'])
acceptable_solution = float(config['EndCondition']['acceptable_solution'])
structure_percentage = float(config['EndCondition']['structure_percentage'])
by_content = config.getboolean('EndCondition', 'by_content')

result = genetic_algorithm(population_amount, character_type, selection_method1, selection_method2, selection_amount,
                           selection_probability, crossing_method, mutation_probability, multi_gen, uniform,
                           replacement_method1, replacement_method2, replacement_probability, number_iterations,
                           acceptable_solution, structure_percentage, by_content)

# mutation_rate = config.getfloat('GeneticAlgorithm', 'mutation_rate')
# selection_method = config.get('GeneticAlgorithm', 'selection_method')

# # Chargement des données des personnages depuis le fichier JSON
# with open('characters_data.json', 'r') as file:
#     characters_data = json.load(file)

# # Accéder aux caractéristiques d'un personnage
# warrior_attributes = characters_data['warrior']
# archer_attributes = characters_data['archer']
