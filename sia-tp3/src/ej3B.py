import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from perceptron_mul import MultilayerPerceptron  

def load_data(file_path):
    data = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            data.append(row)
    
    return np.array(data)

def run():
    # Cargar datos desde el archivo
    file_path = "sia-tp3\data\TP3-ej3-digitos.txt"
    data = load_data(file_path)
    
    input_size = 5  # Ajusta este valor según el número de columnas en tu archivo
    hidden_size = 4  # Ajusta este valor según sea necesario
    output_size = 1
    learning_rate = 0.1
    epochs = 10000

    # Crear etiquetas (1 para números pares, 0 para números impares)
    labels = np.array([1 if np.sum(row) % 2 == 0 else 0 for row in data]).reshape(-1, 1)

    # Dividir el conjunto de datos en entrenamiento y prueba (por ejemplo, 80% entrenamiento y 20% prueba)
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    mlp = MultilayerPerceptron(input_size, hidden_size, output_size, learning_rate)

    # Entrenar con Gradiente Descendente y medir el tiempo
    start_time = time.time()
    mlp.train_with_gradient_descent(X_train, y_train, epochs)
    end_time = time.time()
    print(f"Tiempo de entrenamiento con Gradiente Descendente: {end_time - start_time} segundos")

    # Hacer predicciones con Gradiente Descendente
    predictions = mlp.predict(X_test)
    accuracy = accuracy_score(y_test, (predictions >= 0.5).astype(int))
    print(f"Precisión con Gradiente Descendente: {accuracy * 100:.2f}%")

    # Entrenar con Adam y medir el tiempo
    start_time = time.time()
    mlp.train_with_adam(X_train, y_train, epochs)
    end_time = time.time()
    print(f"Tiempo de entrenamiento con Adam: {end_time - start_time} segundos")

    # Hacer predicciones con Adam
    predictions = mlp.predict(X_test)
    accuracy = accuracy_score(y_test, (predictions >= 0.5).astype(int))
    print(f"Precisión con Adam: {accuracy * 100:.2f}%")