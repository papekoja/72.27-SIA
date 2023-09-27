import numpy as np  
from perceptron_mul import MultilayerPerceptron  

class ej3A:
    def __init__(self):
        input_size = 2
        hidden_size = 4
        output_size = 1
        learning_rate = 0.1
        self.epochs = 10000

        self.mlp = MultilayerPerceptron(input_size, hidden_size, output_size, learning_rate)


    def train(self):
        # Datos de entrada
        X = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
        # Etiquetas de salida
        y = np.array([[1], [1], [-1], [-1]])

        # Entrenar la red neuronal
        self.mlp.train(X, y, self.epochs)

    def predict(self, input_data):
        # Hacer predicciones
        predictions = self.mlp.predict(input_data)
        return predictions

    def main():
        # Crear una instancia de ej3A
        my_model = ej3A()

        # Entrenar el modelo
        my_model.train()

        # Datos de entrada para hacer predicciones
        input_data = np.array([[1, 1], [-1, 1]])

        # Realizar predicciones
        predictions = my_model.predict(input_data)

        # Imprimir las predicciones
        print("Predicciones:")
        for i, prediction in enumerate(predictions):
            print(f"Entrada {i + 1}: {prediction[0]}")
    

