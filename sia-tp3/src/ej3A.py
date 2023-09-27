import numpy as np
from perceptron_mul import MultilayerPerceptron 

def run():
    # Definir las entradas (X) y las salidas esperadas (y) para la función XOR
    X = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    y = np.array([1, 1, -1, -1])

    # Definir hiperparámetros
    input_size = 2
    hidden_size = 4
    output_size = 1
    learning_rate = 0.1
    epochs = 10000

    # Crear una instancia del perceptrón con Gradiente Descendente
    mlp_gradient_descent = MultilayerPerceptron(input_size, hidden_size, output_size, learning_rate)

    # Entrenar con Gradiente Descendente
    mlp_gradient_descent.train_with_gradient_descent(X, y.reshape(-1, 1), epochs)

    # Crear una instancia del perceptrón con el optimizador Adam
    mlp_adam = MultilayerPerceptron(input_size, hidden_size, output_size, learning_rate)

    # Entrenar con el optimizador Adam
    mlp_adam.train_with_adam(X, y.reshape(-1, 1), epochs)

    # Probar el modelo entrenado con XOR
    test_input = np.array([[1, -1]])
    output_gradient_descent = mlp_gradient_descent.predict(test_input)
    output_adam = mlp_adam.predict(test_input)

    print("Resultado con Gradiente Descendente:", output_gradient_descent)
    print("Resultado con Adam:", output_adam)
