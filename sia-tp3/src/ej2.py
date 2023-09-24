import pandas as pd
import perceptron
from sklearn.model_selection import train_test_split

# Read the CSV file into a DataFrame
df = pd.read_csv('sia-tp3\data\TP3-ej2-conjunto.csv')

print(df.head())

df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

def run():
    p = perceptron.Perceptron()
    p.train(df_train)
    p.predict(df_test)

run()