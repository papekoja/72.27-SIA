import numpy as np

def uniform_mutation(new_population, mutation_rate):
    for individual in new_population:
        if np.random.uniform() < mutation_rate:
            individual.mutate()
            
#def non_uniform_mutation(new_population, mutation_rate):