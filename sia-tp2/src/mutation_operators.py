import random
import numpy as np


def mutate_population(children, mutation_probability, multi_gen=False):
    for child in children:
        if not multi_gen:
            if random.random() < mutation_probability:
                mutate_gene(child, random.randint(0, 149))
            elif random.random() < mutation_probability:
                mutate_gene(child, random.randint(150, 155))
        else:
            if random.random() < mutation_probability:
                mutate_gene(child, random.randint(0, 149))
            if random.random() < mutation_probability:
                mutate_gene(child, random.randint(150, 155))


# The gene1 is a list of 150 elements where each element is a letter while the gene2 is a list of 6 elements where each element is a bit.
# Depending on the gene_index, the function will mutate the gene1 or the gene2.
def mutate_gene(child, gene_index):
    if gene_index < 150:
        child.gene1[gene_index] = random.choice(['s', 'a', 'e', 'r', 'h'])
    else:
        child.gene2[gene_index - 150] = 1 - child.gene2[gene_index - 150]
