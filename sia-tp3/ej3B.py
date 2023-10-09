import numpy as np
from perceptron_mul_2 import perceptron_mul_2


# Define a function to read and parse the digit data
def read_digit_data(filename):
    digit_images = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            # Take 5 lines to form a 5x5 matrix
            matrix_lines = lines[i:i+5]
            # Extract and parse values from the matrix lines
            values = []
            for line in matrix_lines:
                values.extend([int(value) for value in line.split()])
            # Convert the list of values into a 5x5 numpy array
            digit_image = np.array(values).reshape(5, 5)
            digit_images.append(digit_image)
    return digit_images

# Usage:
filename = 'sia-tp3\data\TP3-ej3-digitos.txt'
digit_images = read_digit_data(filename)

# Now digit_images contains a list of 5x5 matrices representing the digits


# Define the perceptron_mul_2 class (include the class definition here)

# Load digit images and labels
digit_images = read_digit_data('sia-tp3\data\TP3-ej3-digitos.txt')

# Define labels for each digit (assuming a sequential order from 0 to 9)
labels = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1]

# Convert the list of digit images to a numpy array for easier manipulation
X = np.array(digit_images)

# Initialize an instance of the perceptron_mul_2 class
perceptron = perceptron_mul_2()

# Train the neural network using the digit images and labels
iterations = 1000  # Adjust the number of iterations as needed
learning_rate = 0.01  # Adjust the learning rate as needed
perceptron.gradient_descent(X, labels, iterations, learning_rate)

# Now you have a trained neural network that can predict labels for digit images.
# You can use perceptron.test_predictions(X_test) to make predictions on new data.


