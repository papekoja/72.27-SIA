import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

# Global variable
factory = PokemonFactory("pokemon.json")

def load_config(file_path):
    with open(file_path, "r") as f:
        config = json.load(f)
    return config

def run_iteration(pokemon, pokeball, iters, noise):
    success = 0
    for _ in range(iters):  # Use _ as a placeholder for the loop variable since it's not used
        result, _ = attempt_catch(pokemon, pokeball, noise)  # Unused variable rate removed
        if result:  # No need to compare with True explicitly
            success += 1
    return success, iters  # Return as a tuple

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <config_file>")
        sys.exit(1)
    
    config = load_config(sys.argv[1])
    pokeballs = config["pokeballs"]
    pokemons_name = config["pokemons"]
    
    # # 1.
    # # Initialize a list to store general pokeball success rates
    # general_pokeball_success_rate = []
    # # Iterate through each pokeball type
    # for pokeball in pokeballs:
    #     total_success = 0
    #     total_try = 0
    #     # Initialize lists to store success rates and x-axis labels
    #     pokeball_success_rate = []
    #     x_axis = pokemons_name.copy()  # Make a copy to avoid modifying the original list
    #     # Iterate through each pokemon name
    #     for pokemon_name in pokemons_name:
    #         pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
    #         success, iters = run_iteration(pokemon, pokeball, 100, 0)
    #         pokeball_success_rate.append(success / iters)
    #         total_success += success
    #         total_try += iters
        
    #     # Calculate and append the total success rate for the pokeball
    #     pokeball_success_rate.append(total_success / total_try)
    #     x_axis.append("Total")
        
    #     general_pokeball_success_rate.append(total_success / total_try)
        
    #     # b) Create a DataFrame and plot a bar chart
    #     data = {
    #         "Pokemons": x_axis,
    #         "Success_Rate": pokeball_success_rate, 
    #     }
    #     df = pd.DataFrame(data)
    #     # print(df)
    #     fig = px.bar(df, x="Pokemons", y="Success_Rate", color="Pokemons", text_auto=True, title=f"Success rate for each pokemon for {pokeball}")
    #     # fig.show()
    
    # # a) Create a DataFrame for general pokeball success rates and plot a bar chart
    # data = {
    #     "Pokeballs": pokeballs,
    #     "Success_Rate": general_pokeball_success_rate,
    # }
    # df = pd.DataFrame(data)
    # print(df)
    # fig = px.bar(df, x="Pokeballs", y="Success_Rate", color="Pokeballs", text_auto=True, title="General success rate for each Pokeball")
    # fig.show()
    
    # 2.
    # a)

    # columns = ["Pokeballs", "Effect", "Rate"]
    # df = pd.DataFrame(columns=columns)

    # for pokeball in pokeballs:
    #     for effect in StatusEffect:
    #         total_success = 0
    #         total_try = 0

    #         # Iterate through each pokemon name
    #         for pokemon_name in pokemons_name:
    #             pokemon = factory.create(pokemon_name, 100, effect, 1)
    #             success, iters = run_iteration(pokemon, pokeball, 50, 0)
    #             total_success += success
    #             total_try += iters
    #         new_row = {"Pokeballs": pokeball, "Effect": effect.name, "Rate": total_success/total_try}
    #         df = df._append(new_row, ignore_index=True)
    # # print(df)
    # fig = px.bar(df, x="Pokeballs", y="Rate", color="Effect", barmode="group")
    # fig.show()

    

    # b)
    # Only using "snorlax" as a pokemon

    # columns = ["Pokeballs", "Effect", "Rate", "Health"]    
    # points = 1500
    # healths = [i/points for i in range(points+1)]

    # df2 = pd.DataFrame(columns=columns)
    # # pokeballs = ["ultraball"]
    # # StatusEffect = [StatusEffect.NONE]

    # for pokeball in pokeballs:              # 4 pokeballs

    #     for effect in StatusEffect:         # 5 satuseffects
    #         total_success = 0
    #         total_try = 0

    #         for healt in healths:           # 4 healths

    #             pokemon = factory.create("snorlax", 100, effect, healt)
    #             success, iters = run_iteration(pokemon, pokeball, 50, 0)
    #             total_success += success
    #             total_try += iters
    #             new_row = {"Pokeballs": pokeball, "Effect": effect.name, "Rate": total_success/total_try, "Health": healt}
    #             df2 = df2._append(new_row, ignore_index=True)
    
    # # fig = px.bar(df2, x="Pokeballs", y="Rate", color="Effect", barmode="group")
    # fig = px.scatter(df2, x="Health", y="Rate", color="Pokeballs")
    
    # fig.update_layout(title="Success rate only for snorlax with four balls, no effect and different healths")

    # fig.show()


    # ---------------------------------------------- #


    points = 100
    healths = [i/points for i in range(points+1)]
    levels_manual = [50, 100, 200]

    parameter_grid = {
        'pokemon': pokemons_name,
        'effect': StatusEffect,
        'pokeball': pokeballs,
        'health': healths,
        'level': levels_manual
    }

    highest_rate = 0
    best_params = {}
    double_best_params = False
    
    columns = ["Pokemon", "Effect", "Rate", "Health", "Pokeballs"]
    pokemons_manual = ["mewtwo", "caterpie"]
    # pokemons_manual = ["jolteon", "caterpie", "snorlax", "onix", "mewtwo"]

    df3 = pd.DataFrame(columns=columns)

    for pokemon_for_loop in parameter_grid['level']:
        for effect in parameter_grid['effect']:
            for pokeball in parameter_grid['pokeball']:
                for health in parameter_grid['health']:

                    pokemon = factory.create('mewtwo', 100, effect, health)
                    success, iters = run_iteration(pokemon, pokeball, pokemon_for_loop, 0)
                    
                    iter_success_rate = success/iters
                    
                    new_row = {"Pokeballs": pokeball, "Effect": effect.name, "Rate": iter_success_rate, "Health": health, "Pokemon": pokemon.name, "Level": pokemon_for_loop}
                    df3 = df3._append(new_row, ignore_index=True)

                    if iter_success_rate > highest_rate:
                        highest_rate = iter_success_rate
                        best_params = {"Pokeballs": pokeball, "Effect": effect.name, "Rate": iter_success_rate, "Health": health, "Pokemon": pokemon.name, "Level": pokemon_for_loop}

                    if iter_success_rate == highest_rate:
                        double_best_params = True


    print(f"\nSuccess\n{best_params}")

    fig = px.scatter(
        df3,
        x="Health",
        y="Rate",
        color="Effect",
        facet_col="Level",  # Creates subplots for each Pokemon
        facet_row="Pokeballs",  # Creates subplots for each Pokeball
        category_orders={"Pokemon": pokemons_manual, "Pokeballs": pokeballs},  # Order for facets
        labels={"Pokemon": "Pokemon", "Pokeballs": "Pokeball"},  # Labels for facet categories
        trendline="ols",
    )

    fig.update_layout(
        title="Influence of Parameters on Success Rate",
        yaxis_title="Success Rate",
        xaxis_title="Health",
        height=1200,  # Set the height of the whole figure
        width=2000,  # Set the width of the whole figure
    )

    fig.show()

    # plot_html_file = "graphs/2c_scatter_plot2.html"
    # fig.write_html(plot_html_file)



