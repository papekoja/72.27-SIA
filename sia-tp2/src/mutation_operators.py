import random
import numpy as np

def mutate_population(population, pm, multigen = False):
    for character in population:
        if random.random() < pm:
            startindex = random.randint(0, 155)
            if multigen:
                endindex = random.randint(startindex, 155)
                for i in range(startindex, endindex):
                    mutate_gene(character, i)
            else:
                mutate_gene(character, startindex)


# The gene1 is a list of 150 elements where each element is a letter while the gene2 is a list of 6 elements where each element is a bit.
# Depending on the gene_index, the function will mutate the gene1 or the gene2.
def mutate_gene(character, gene_index):
    if gene_index < 150:
        character.gene1[gene_index] = np.random.choice(['s', 'a', 'e', 'r', 'h'])
    else:
        print("gene2")
        character.gene2[gene_index] = 1 - character.gene2[gene_index - 150]