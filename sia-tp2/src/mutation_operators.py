import random

ITEM_NUMBER = 15000


def mutate_population(children, mutation_probability, multi_gen=False):
    for child in children:
        if not multi_gen:
            if random.random() < mutation_probability:
                mutate_gene(child, random.randint(0, ITEM_NUMBER - 1))
            elif random.random() < mutation_probability:
                mutate_gene(child, random.randint(ITEM_NUMBER, ITEM_NUMBER + 5))
        else:
            if random.random() < mutation_probability:
                mutate_gene(child, random.randint(0, ITEM_NUMBER - 1))
            if random.random() < mutation_probability:
                mutate_gene(child, random.randint(ITEM_NUMBER, ITEM_NUMBER + 5))


# The gene1 is a list of 15000 elements where each element is a letter while the gene2 is a list of 6 elements where each element is a bit.
# Depending on the gene_index, the function will mutate the gene1 or the gene2.
def mutate_gene(child, gene_index):
    if gene_index < ITEM_NUMBER:
        child.gene1[gene_index] = random.choice(['s', 'a', 'e', 'r', 'h'])
    else:
        child.gene2[gene_index - ITEM_NUMBER] = 1 - child.gene2[gene_index - ITEM_NUMBER]
