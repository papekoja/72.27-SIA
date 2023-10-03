import numpy as np
import pandas as pd

# Read the input data from the text file
with open('sia-tp3/data/TP3-ej3-digitos.txt', 'r') as file:
    lines = file.readlines()

# Parse the lines and create a list of lists
data = []
for line in lines:
    row = [int(x) for x in line.strip().split()]
    data.append(row)

# Convert the list of lists into a NumPy array
data = np.array(data)

# 7 rows is one image. Split the input array into 7 rows each
numbers = np.split(data, 10)

numbers = np.array(numbers)

class perceptron_mul_2:
    def __init__(self):
        # Create weights for the first layer (input is 0th). 10 neurons, 35 inputs(5x7)
        self.W1 = np.random.rand(10, 35)
        # Create bias for first layer
        self.B1 = np.random.rand(10, 1)
        # Create weights for the second layer (input is 1st). 10 neurons, 10 inputs
        self.W2 = np.random.rand(10, 10)
        # Create bias for second layer
        self.B2 = np.random.rand(10, 1)

    def relu(self, Z):
        return np.maximum(0, Z)
    
    def softmax(self, Z):
        return np.exp(Z) / np.sum(np.exp(Z), axis=0)

    def forward_prop(self, X):
        # First layer
        Z1 = self.W1.dot(X) + self.B1
        A1 = self.relu(Z1)
        # Second layer
        Z2 = self.W2.dot(A1) + self.B2
        A2 = self.softmax(Z2)
        return Z1, A1, Z2, A2
    
    # One hot encoding of the output labels (Y). There are 10 classes (Y.max()+1, 0-9)
    def one_hot(self, Y):
        one_hot_Y = np.zeros((Y.size, Y.max()+1))
        one_hot_Y[np.arange(Y.size), Y] = 1
        one_hot_Y = one_hot_Y.T
        return one_hot_Y
    
    def deriv_relu(self, Z):
        return Z > 0

    def back_prop(self, Z1, A1, Z2, A2, X, Y):
        m = Y.size
        one_hot_Y = self.one_hot(Y)
        dZ2 = A2 - one_hot_Y
        dW2 = 1/m * dZ2.dot(A1.T)
        db2 = 1 / m * np.sum(dZ2)
        dZ1 = self.W2.T.dot(dZ2)
        dW1 = 1 / m * dZ1.dot(X.T)
        db1 = 1 / m * np.sum(dZ1)
        return dW1, db1, dW2, db2
    
    def uptade_params(self, dW1, db1, dW2, db2, learning_rate):
        self.W1 -= learning_rate * dW1
        self.B1 -= learning_rate * db1
        self.W2 -= learning_rate * dW2
        self.B2 -= learning_rate * db2

    def get_predictions(self, A2):
        return np.argmax(A2, 0)
    
    def getAccuracy(self, predictions, Y):
        print(predictions, Y)
        return np.sum(predictions == Y) / Y.size
    
    def gradient_descent(self, X, Y, iternations, alpha):
        for i in range(iternations):
            Z1, A1, Z2, A2 = self.forward_prop(X)
            dW1, db1, dW2, db2 = self.back_prop(Z1, A1, Z2, A2, X, Y)
            self.uptade_params(dW1, db1, dW2, db2, alpha)
            if i % 50 == 0:
                print("Iternation: ", i) 
                print("Accyracy: ", self.getAccuracy(self.get_predictions(A2), Y))
        return self.W1, self.B1, self.W2, self.B2

def generate_data(qty, noise_precentage):
    X = []
    Y = []
    for i in range(qty):
        rnd = np.random.randint(0, 10)
        n = noise_picture(numbers[rnd], noise_precentage)
        X.append(n.flatten())
        Y.append(rnd)
    return np.array(X).T, np.array(Y)

def noise_picture(array, flip_probability):

    # Generate a random boolean mask with the same shape as the array
    random_mask = np.random.random(size=array.shape) < flip_probability

    # Use the mask to flip the values (change ones to zeros and zeros to ones)
    noisy_array = np.logical_xor(array, random_mask).astype(int)
    return noisy_array

p = perceptron_mul_2()
X_train, Y_train = generate_data(50, 0.1)
p.gradient_descent(X_train, Y_train , 100, 0.1)