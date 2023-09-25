import pandas as pd
import perceptron
from sklearn.model_selection import train_test_split

# Read the CSV file into a DataFrame
df = pd.read_csv('sia-tp3\data\TP3-ej2-conjunto.csv')
_, df_test = train_test_split(df, test_size=0.5, random_state=42)


def run():
    bootstrap_perceptron = bootstrapping(20, 10)
    _, bootstrap_mse = bootstrap_perceptron.predict(df_test)
    print("Bootstrap Perceptron MSE:", bootstrap_mse)
    random_perceptron = random_selection(0.2)
    _, random_mse = random_perceptron.predict(df_test)
    print("Random Perceptron MSE:", random_mse)

def bootstrapping(sample_size, iterations):
    perceptrons = pd.DataFrame(columns=['w1', 'w2', 'w3', 'b'])
    for i in range(iterations):
        temp_df = df.sample(n=sample_size, random_state=42)
        p = perceptron.Perceptron()
        p.train(temp_df)
        w1, w2, w3, b = p.get_weights()
        perceptrons.loc[len(perceptrons)] = [w1, w2, w3, b]
    return perceptron.Perceptron()

def random_selection(test_size):
    df_train, df_test = train_test_split(df, test_size=test_size, random_state=42)
    p = perceptron.Perceptron()
    p.train(df_train)
    return p

run()