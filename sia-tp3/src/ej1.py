import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from perceptron import Perceptron

# Función para entrenar y probar el perceptrón en un problema lógico
def train_and_test_logical_function(x, y, function_name):
    print(f"Entrenando para la función lógica {function_name}")
    
    # Crear un DataFrame con los datos de entrada y salida esperada
    data = pd.DataFrame({'x1': x[:, 0], 'x2': x[:, 1], 'y': y})
    
    # Crear una instancia del perceptrón
    perceptron = Perceptron()
    
    # Entrenar el perceptrón
    perceptron.train1(data)
    
    # Realizar predicciones
    predictions = perceptron.predict1(data)
    
    # Imprimir resultados
    print("Resultados:")
    print(predictions)
    print("\nPesos finales del perceptrón:")
    print(perceptron.get_weights())

# Definir datos de entrada y salidas esperadas para las funciones lógicas "Y" y "O exclusivo"
x_and = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
y_and = np.array([-1, -1, -1, 1])

x_xor = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
y_xor = np.array([1, 1, -1, -1])

# Entrenar y probar el perceptrón para la función lógica "Y"
train_and_test_logical_function(x_and, y_and, "Y")

# Entrenar y probar el perceptrón para la función lógica "O exclusivo"
train_and_test_logical_function(x_xor, y_xor, "O exclusivo")




# Función para entrenar y probar el perceptrón en un problema lógico y mostrar gráficas
def train_and_test_logical_function_with_plots(x, y, function_name):
    print(f"Entrenando para la función lógica {function_name}")
    
    # Crear un DataFrame con los datos de entrada y salida esperada
    data = pd.DataFrame({'x1': x[:, 0], 'x2': x[:, 1], 'y': y})
    
    # Crear una instancia del perceptrón
    perceptron = Perceptron()
    
    # Listas para almacenar los cambios de pesos y errores durante el entrenamiento
    weight_changes = []
    errors = []
    
    # Entrenar el perceptrón
    for epoch in range(100):  # Número de épocas de entrenamiento
        perceptron.train1(data)  # Utiliza train1 para entrenar solo con x1 y x2
        weight_changes.append(perceptron.get_weights())
        predictions = perceptron.predict1(data)  # Utiliza predict1 para hacer predicciones con x1 y x2
        errors.append(np.mean(np.abs(data['y'] - predictions['y_pred'])))  # Compara con 'y' en lugar de 'y_pred'
    
    # Crear gráficas
    plt.figure(figsize=(12, 5))
    
    # Gráfica de los cambios en los pesos a lo largo del entrenamiento
    plt.subplot(1, 2, 1)
    weight_changes = np.array(weight_changes)
    plt.plot(weight_changes[:, 0], label='W1')
    plt.plot(weight_changes[:, 1], label='W2')
    plt.plot(weight_changes[:, 2], label='B')
    plt.xlabel('Época')
    plt.ylabel('Peso')
    plt.legend()
    plt.title('Cambios en los pesos durante el entrenamiento')
    
    # Gráfica del error a lo largo del entrenamiento
    plt.subplot(1, 2, 2)
    plt.plot(errors)
    plt.xlabel('Época')
    plt.ylabel('Error')
    plt.title('Error durante el entrenamiento')
    
        # Gráfica de las predicciones
#    plt.subplot(1, 3, 3)
#    plt.scatter(data['x1'], data['x2'], c=data['y'], cmap='viridis', label='Real')
#    plt.scatter(data['x1'], data['x2'], c=predictions['y_pred'], cmap='viridis', marker='x', label='Predicción')
#    plt.xlabel('x1')
#   plt.ylabel('x2')
#   plt.legend()
#    plt.title('Predicciones')
#
    plt.tight_layout()
    plt.show()

# Entrenar y probar el perceptrón para la función lógica "Y" con gráficas
train_and_test_logical_function_with_plots(x_and, y_and, "Y")

# Entrenar y probar el perceptrón para la función lógica "O exclusivo" con gráficas
train_and_test_logical_function_with_plots(x_xor, y_xor, "O exclusivo")
