import configparser
import json
import numpy as np

from src.genetic_algorithm import genetic_algorithm

number_parents = 100
number_iterations = 2
selection_method = 'elite'

result = genetic_algorithm(number_parents, number_iterations, selection_method)


# print(result)










# config = configparser.ConfigParser()
# config.read('config.ini')

# mutation_rate = config.getfloat('GeneticAlgorithm', 'mutation_rate')
# selection_method = config.get('GeneticAlgorithm', 'selection_method')

# # Chargement des données des personnages depuis le fichier JSON
# with open('characters_data.json', 'r') as file:
#     characters_data = json.load(file)

# # Accéder aux caractéristiques d'un personnage
# warrior_attributes = characters_data['warrior']
# archer_attributes = characters_data['archer']
