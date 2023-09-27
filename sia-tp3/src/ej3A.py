import numpy as np
from perceptron_mul import MultilayerPerceptron
import matplotlib.pyplot as plt

class ej3A:
    def __init__(self, optimizer="gd"):
        input_size = 1
        hidden_size = 4
        output_size = 1
        learning_rate = 0.1
        self.epochs = 10000

        if optimizer == "gd":
            self.mlp = MultilayerPerceptron(input_size, hidden_size, output_size, learning_rate)
        elif optimizer == "adam":
            self.mlp = MultilayerPerceptron(input_size, hidden_size, output_size, learning_rate)

    def train(self, X, y):
        # Entrenar la red neuronal
        self.mlp.train(X, y, self.epochs)

    def predict(self, input_data):
        # Hacer predicciones
        predictions = self.mlp.predict(input_data)
        return predictions

def run():
    # Datos de entrada
    X = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    # Etiquetas de salida
    y = np.array([[1], [1], [-1], [-1]])

    # Crear una instancia de ej3A para Gradiente Descendente (gd)
    gd_model = ej3A(optimizer="gd")
    # Entrenar el modelo con Gradiente Descendente
    gd_model.train(X, y)

    # Crear una instancia de ej3A para Adam
    adam_model = ej3A(optimizer="adam")
    # Entrenar el modelo con Adam
    adam_model.train(X, y)

    # Datos de entrada para hacer predicciones
    input_data = np.array([[1, 1], [-1, 1]])

    # Realizar predicciones con Gradiente Descendente
    gd_predictions = gd_model.predict(input_data)

    # Realizar predicciones con Adam
    adam_predictions = adam_model.predict(input_data)

    # Crear gráfica comparativa
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Predicciones con Gradiente Descendente")
    plt.bar([f"Entrada {i+1}" for i in range(len(gd_predictions))], gd_predictions.flatten())

    plt.subplot(1, 2, 2)
    plt.title("Predicciones con Adam")
    plt.bar([f"Entrada {i+1}" for i in range(len(adam_predictions))], adam_predictions.flatten())

    plt.tight_layout()
    plt.show()