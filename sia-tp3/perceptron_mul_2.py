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
        self.W1 = np.random.rand(10, 35) - 0.5
        # Create bias for first layer
        self.B1 = np.random.rand(10, 1) - 0.5
        # Create weights for the second layer (input is 1st). 10 neurons, 10 inputs
        self.W2 = np.random.rand(10, 10) - 0.5
        # Create bias for second layer
        self.B2 = np.random.rand(10, 1) - 0.5

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
        return np.sum(predictions == Y) / Y.size
    
    def gradient_descent(self, X, Y, iternations, alpha):
        for i in range(iternations):
            Z1, A1, Z2, A2 = self.forward_prop(X)
            dW1, db1, dW2, db2 = self.back_prop(Z1, A1, Z2, A2, X, Y)
            self.uptade_params(dW1, db1, dW2, db2, alpha)
            if i % 50 == 0:
                print("Iternation: ", i) 
                print("Accuracy: ", self.getAccuracy(self.get_predictions(A2), Y))
        return self.W1, self.B1, self.W2, self.B2
    
    def make_predictions(self, X):
        _, _, _, A2 = self.forward_prop(X)
        return self.get_predictions(A2)


def generate_data(qty, noise_precentage):
    X = []
    Y = []
    for i in range(qty):
        n = np.random.randint(0, 10)
        pic = noise_data(numbers[n], noise_precentage)
        X.append(pic.flatten())
        Y.append(n)
    X = np.array(X)
    Y = np.array(Y)
    return X.T, Y

def noise_data(X, precentage):
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if np.random.rand() < precentage:
                X[i][j] = 1 if X[i][j] == 0 else 0
    return X

p = perceptron_mul_2()
X_train, Y_train = generate_data(1000, 0)
X_test, Y_test = generate_data(1000, 0)

for i in range(20):
    print("X: ", X_train[:, i], "Y: ", Y_train[i])

p.gradient_descent(X_train, Y_train , 300, 0.1)

predictions = p.make_predictions(X_test)
for i in range(10):
    print("Prediction: ", predictions[i], "Actual: ", Y_test[i])
print("Accuracy: ", p.getAccuracy(predictions, Y_test))