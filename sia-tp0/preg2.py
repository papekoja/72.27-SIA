import json
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

# Global variable
factory = PokemonFactory("pokemon.json")

def load_config(file_path):
    with open(file_path, "r") as f:
        config = json.load(f)
    return config
config = load_config("./config/all.json")
pokeballs = config["pokeballs"]
pokemonNames = config["pokemons"]

columns = ["Pokemon", "Pokeball", "Health", "Catch Rate"]
df = pd.DataFrame(columns=columns)
df['Pokemon'] = np.nan
df['Pokeball'] = np.nan
df['Health'] = np.nan
df['Catch Rate'] = np.nan

def runTests():
    pokeball = pokeballs[0]
    for i in range(0,2):
        pokeName = pokemonNames[i]
        for j in range(0, 1000):
            pokemon = factory.create(pokeName, 100, StatusEffect.NONE, random.random())
            _, catchRate = attempt_catch(pokemon, pokeball, 0)
            df.loc[len(df.index)] = [pokeName, pokeball, pokemon.current_hp, catchRate]

runTests()

for name, group in df.groupby('Pokemon'):
    plt.scatter(group['Health'], group['Catch Rate'], label=name)

plt.xlabel('Health Level')
plt.ylabel('Success Rate')
plt.title('Success Rate vs Health Level')
plt.legend()
plt.grid(True)
plt.show()
