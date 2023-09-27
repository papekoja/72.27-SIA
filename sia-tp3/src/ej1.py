import numpy as np
import pandas as pd
from perceptron import Perceptron

def run():
    x_and = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    y_and = np.array([-1, -1, -1, 1])

    x_xor = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    y_xor = np.array([1, 1, -1, -1])

    # Crear y entrenar un Perceptrón para la función "Y"
    perceptron_and = Perceptron()
    perceptron_and.non_linear = False  # Usar función de activación escalón
    df_and = pd.DataFrame(data=np.column_stack((x_and, y_and)), columns=['x1', 'x2', 'y'])
    perceptron_and.train1(df_and)

    # Crear y entrenar un Perceptrón para la función "O exclusivo"
    perceptron_xor = Perceptron()
    perceptron_xor.non_linear = False  # Usar función de activación escalón
    df_xor = pd.DataFrame(data=np.column_stack((x_xor, y_xor)), columns=['x1', 'x2', 'y'])
    perceptron_xor.train1(df_xor)

    # Probar los Perceptrones entrenados
    print("Función lógica 'Y':")
    perceptron_and.test1(df_and)
    print("Predicciones para 'Y':")
    result_and = perceptron_and.predict1(df_and)
    print(result_and)

    print("\nFunción lógica 'O exclusivo':")
    perceptron_xor.test1(df_xor)
    print("Predicciones para 'O exclusivo':")
    result_xor = perceptron_xor.predict1(df_xor)
    print(result_xor)

    # Obtener los pesos de los Perceptrones
    print("\nPesos del Perceptrón para 'Y':")
    print(perceptron_and.get_weights())
    print("\nPesos del Perceptrón para 'O exclusivo':")
    print(perceptron_xor.get_weights())

