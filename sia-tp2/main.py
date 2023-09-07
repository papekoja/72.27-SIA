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
amount_parents = int(config['GeneticAlgorithm']['population_number'])
number_iterations = int(config['GeneticAlgorithm']['max_generations'])
selection_method = str(config['GeneticAlgorithm']['selection_method'])


character = Character("warrior", 30, 30, 30, 30, 30, 1.6)
# print(character)
# mutate_population([character], 20, False)
# print(character)


result = genetic_algorithm(amount_parents, number_iterations, selection_method)










# mutation_rate = config.getfloat('GeneticAlgorithm', 'mutation_rate')
# selection_method = config.get('GeneticAlgorithm', 'selection_method')

# # Chargement des données des personnages depuis le fichier JSON
# with open('characters_data.json', 'r') as file:
#     characters_data = json.load(file)

# # Accéder aux caractéristiques d'un personnage
# warrior_attributes = characters_data['warrior']
# archer_attributes = characters_data['archer']

