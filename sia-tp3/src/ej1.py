import numpy as np
import pandas as pd
from perceptron import Perceptron 
 
def run():
    # Datos de entrada y salida para la función lógica "Y"
    inputs_and = np.array([[-1, 1, 1], [1, -1, 1], [-1, -1, 1], [1, 1, 1]])
    targets_and = np.array([-1, -1, -1, 1])

    # Datos de entrada y salida para la función lógica "O exclusivo"
    inputs_xor = np.array([[-1, 1, 1], [1, -1, 1], [-1, -1, 1], [1, 1, 1]])
    targets_xor = np.array([1, 1, -1, -1])

    # Crear un perceptrón para la función lógica "Y"
    perceptron_and = Perceptron()
    perceptron_and.train(pd.DataFrame({'x1': inputs_and[:, 0], 'x2': inputs_and[:, 1], 'x3': inputs_and[:, 2], 'y': targets_and}))

    # Crear un perceptrón para la función lógica "O exclusivo"
    perceptron_xor = Perceptron()
    perceptron_xor.train(pd.DataFrame({'x1': inputs_xor[:, 0], 'x2': inputs_xor[:, 1], 'x3': inputs_xor[:, 2], 'y': targets_xor}))

    # Probar el perceptrón para la función lógica "Y"
    result_and, mse_and = perceptron_and.predict(pd.DataFrame({'x1': inputs_and[:, 0], 'x2': inputs_and[:, 1], 'x3': inputs_and[:, 2], 'y': targets_and}))
    print("Predicciones para la función 'Y':")
    print(result_and)
    print("MSE para la función 'Y':", mse_and)

    # Probar el perceptrón para la función lógica "O exclusivo"
    result_xor, mse_xor = perceptron_xor.predict(pd.DataFrame({'x1': inputs_xor[:, 0], 'x2': inputs_xor[:, 1], 'x3': inputs_xor[:, 2], 'y': targets_xor}))
    print("\nPredicciones para la función 'O exclusivo':")
    print(result_xor)
    print("MSE para la función 'O exclusivo':", mse_xor)
