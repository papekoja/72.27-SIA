import numpy as np


class Character:
    # The gene1 consists of repetitions of each letters in character where the number of repetitions is the value of the attribute.
    # The gene2 is the binary representation of the height of the character.
    def __init__(self, type, strength, agility, expertise, resistance, health, height, gene1=None, gene2=None):
        self.type = type
        self.gene1 = gene1
        self.gene2 = gene2
        if not gene1 and not gene2:
            self.gene1 = []
            self.gene2 = []
            self.strength = strength
            self.agility = agility
            self.expertise = expertise
            self.resistance = resistance
            self.health = health
            self.height = height
            attributes = [strength, agility, expertise, resistance, health]

            characters = ['s', 'a', 'e', 'r', 'h']
            for attr, char in zip(attributes, characters):
                for i in range(int(attr * 100)):
                    self.gene1.append(char)
            while len(self.gene1) < 15000:
                self.gene1.append('h')
            while len(self.gene1) > 15000:
                self.gene1.pop()

            binary_representation = bin(int((height - 1.3) * 100))[
                                    2:]  # Get binary representation and remove '0b' prefix
            binary_representation = '0' * (6 - len(binary_representation)) + binary_representation
            self.gene2 = [int(bit) for bit in binary_representation]

        else:
            self.strength = gene1.count('s') / 100
            self.agility = gene1.count('a') / 100
            self.expertise = gene1.count('e') / 100
            self.resistance = gene1.count('r') / 100
            self.health = gene1.count('h') / 100

            binary_string = ''.join(str(bit) for bit in gene2)
            decimal_integer = int(binary_string, 2)
            self.height = 1.3 + (decimal_integer / (2 ** len(gene2) - 1)) * 0.7

        # self.fitness = self.get_fitness()

    def __str__(self):
        return (str(self.type) +
                '(' + str(self.strength) + ','
                + str(self.agility) + ','
                + str(self.expertise) + ','
                + str(self.resistance) + ','
                + str(self.health) + ','
                + str(self.height) + ')')

    def get_fitness(self):
        strength_p = 100 * np.tanh(0.01 * self.strength)
        agility_p = np.tanh(0.01 * self.agility)
        expertise_p = 0.6 * np.tanh(0.01 * self.expertise)
        resistance_p = np.tanh(0.01 * self.resistance)
        life_p = 100 * np.tanh(0.01 * self.health)
        atm = 0.5 - pow((3 * self.height - 5), 4) + pow((3 * self.height - 5), 2) + self.height / 2
        dem = 2 + pow((3 * self.height - 5), 4) - pow((3 * self.height - 5), 2) - self.height / 2
        attack = (agility_p + expertise_p) * strength_p * atm
        defense = (resistance_p + expertise_p) * life_p * dem
        if self.type == 'warrior':
            return 0.6 * attack + 0.4 * defense
        elif self.type == 'archer':
            return 0.9 * attack + 0.1 * defense
        elif self.type == 'defender':
            return 0.1 * attack + 0.9 * defense
        elif self.type == 'undercover':
            return 0.8 * attack + 0.3 * defense

    def equals(self, other_character):
        if isinstance(other_character, Character):
            return (self.strength == other_character.strength and
                    self.agility == other_character.agility and
                    self.expertise == other_character.expertise and
                    self.resistance == other_character.resistance and
                    self.health == other_character.health and
                    self.height == other_character.height)
        return False

    # getters and setters for gene1 and gene2
    def get_gene1(self):
        return self.gene1

    def get_gene2(self):
        return self.gene2

    def set_gene1(self, gene1):
        self.gene1 = gene1

    def set_gene2(self, gene2):
        self.gene2 = gene2

    def get_stats(self):
        return self.type, self.strength, self.agility, self.expertise, self.resistance, self.health, self.height
