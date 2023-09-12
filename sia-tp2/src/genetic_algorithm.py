import math
import random

from src.character import Character
from src.crossing_operators import crossing_operator
from src.mutation_operators import mutate_population
from src.replacement_methods import replacement_method
from src.selection_methods import selection_method


def genetic_algorithm(population_amount, character_type, selection_method1, selection_method2, selection_amount,
                      selection_probability, crossing_method, mutation_probability, multi_gen, uniform,
                      replacement_method1, replacement_method2, replacement_probability, number_iterations,
                      acceptable_solution, structure_percentage, by_content):
    population = []
    generation_tracker = []
    generation = 0
    selection_number1 = math.ceil(selection_amount * selection_probability)
    selection_number2 = selection_amount - selection_number1
    replacement_number1 = math.ceil(population_amount * replacement_probability)
    replacement_number2 = population_amount - replacement_number1

    # Generation 1
    for i in range(population_amount):
        s, a, e, r, h, height = random_stats_generator()
        population.append(Character(character_type, s, a, e, r, h, height))

    generation_tracker.append(
        {"max_fitness": max(population, key=lambda x: x.get_fitness()).get_fitness(), "population": population})

    # Generation 2 to n
    while check_end_condition(generation_tracker, generation, number_iterations, acceptable_solution,
                              structure_percentage, by_content):
        generation += 1
        print(generation)
        children = []

        # SELECTION
        selected_population1 = selection_method(population, selection_method1, selection_number1, generation)
        selected_population2 = selection_method(population, selection_method2, selection_number2, generation)
        selected_population = selected_population1 + selected_population2

        # CROSSING
        for i, j in zip(range(0, selection_amount, 2), range(1, selection_amount, 2)):
            parent1 = selected_population[i]
            parent2 = selected_population[j]
            ch1, ch2, = crossing_operator(parent1, parent2, crossing_method)
            children.append(ch1)
            children.append(ch2)

        # MUTATION
        mutate_population(children, mutation_probability, multi_gen)
        mutation_probability *= 1 if uniform else 0.9

        # REPLACEMENT
        new_population1 = replacement_method(population, replacement_method1, children)
        new_population1 = random.sample(new_population1, replacement_number1)
        new_population2 = replacement_method(population, replacement_method2, children)
        new_population2 = random.sample(new_population2, replacement_number2)
        population = new_population1 + new_population2

        generation_tracker.append(
            {"max_fitness": max(population, key=lambda x: x.get_fitness()).get_fitness(), "population": population})

    print(generation_tracker[-1]["max_fitness"])
    character = max(generation_tracker[-1]["population"], key=lambda x: x.get_fitness())
    print(character)


def random_stats_generator():
    random_numbers = [random.uniform(0, 30) for _ in range(5)]
    total = sum(random_numbers)
    normalized_numbers = [num * 150 / total for num in random_numbers]
    rounded_numbers = [round(num, 2) for num in normalized_numbers]
    while sum(rounded_numbers) != 150:
        diff = 150 - sum(rounded_numbers)
        index_to_adjust = random.randint(0, 4)
        rounded_numbers[index_to_adjust] += diff

    height = random.uniform(1.3, 2.0)

    return rounded_numbers[0], rounded_numbers[1], rounded_numbers[2], rounded_numbers[3], rounded_numbers[4], height


def check_end_condition(generation_tracker, generation, number_iterations, acceptable_solution, structure_percentage,
                        by_content):
    if acceptable_solution > 0:
        last_generation = generation_tracker[generation]
        print(last_generation["max_fitness"])
        return last_generation["max_fitness"] < acceptable_solution
    elif structure_percentage > 0:
        if generation < number_iterations:
            return True
        last_generations = generation_tracker[-number_iterations:]
        last_populations = [last_generation["population"] for last_generation in last_generations]
        for last_population in last_populations:
            last_population.sort(key=lambda x: x.get_fitness(), reverse=True)
        relevant_number = math.ceil(len(last_populations[0]) * structure_percentage)
        relevant_populations = [last_population[:relevant_number] for last_population in last_populations]
        for i in range(1, number_iterations):
            for j in range(relevant_number):
                if relevant_populations[0][j].get_fitness() != relevant_populations[i][j].get_fitness():
                    return True
        return False
    elif by_content:
        if generation < number_iterations:
            return True
        last_generations = generation_tracker[-number_iterations:]
        first_fitness = last_generations[0]["max_fitness"]
        return not all(gen["max_fitness"] == first_fitness for gen in last_generations)
    elif number_iterations is not None:
        return generation < number_iterations
    return False
