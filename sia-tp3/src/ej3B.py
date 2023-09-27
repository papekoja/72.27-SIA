import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
from perceptron_mul import MultilayerPerceptron 
import matplotlib.pyplot as plt  

def load_data(file_path):
    data = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            data.append(row)
    
    return np.array(data)

def plot_training_results(loss_history, accuracy_history, optimizer_name):
    # Plot training loss
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(loss_history)
    plt.title(f'{optimizer_name} - Training Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    # Plot training accuracy
    plt.subplot(1, 2, 2)
    plt.plot(accuracy_history)
    plt.title(f'{optimizer_name} - Training Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')

    plt.tight_layout()
    plt.show()

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

    # Lists to store loss and accuracy history for gradient descent
    gd_loss_history = []
    gd_accuracy_history = []

    # Train with Gradient Descent and record loss and accuracy at each epoch
    for epoch in range(epochs):
        mlp.train_with_gradient_descent(X_train, y_train, 1)
        predictions = mlp.predict(X_train)
        loss = np.mean(0.5 * (y_train - predictions) ** 2)
        accuracy = accuracy_score(y_train, (predictions >= 0.5).astype(int))

        gd_loss_history.append(loss)
        gd_accuracy_history.append(accuracy)

        #if epoch % 100 == 0:
        #    print(f'Epoch {epoch}, Loss: {loss}, Accuracy: {accuracy * 100:.2f}%')

    # Plot Gradient Descent training results
    plot_training_results(gd_loss_history, gd_accuracy_history, 'Gradient Descent')

    # Lists to store loss and accuracy history for Adam
    adam_loss_history = []
    adam_accuracy_history = []

    # Train with Adam and record loss and accuracy at each epoch
    for epoch in range(epochs):
        mlp.train_with_adam(X_train, y_train, 1)
        predictions = mlp.predict(X_train)
        loss = np.mean(0.5 * (y_train - predictions) ** 2)
        accuracy = accuracy_score(y_train, (predictions >= 0.5).astype(int))

        adam_loss_history.append(loss)
        adam_accuracy_history.append(accuracy)

        #if epoch % 100 == 0:
        #    print(f'Epoch {epoch}, Loss: {loss}, Accuracy: {accuracy * 100:.2f}%')

    # Plot Adam training results
    plot_training_results(adam_loss_history, adam_accuracy_history, 'Adam')
