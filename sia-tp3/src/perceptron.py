import numpy as np
import pandas as pd

class Perceptron:
    non_linear = False
    
    def __init__(self):
        self.w1 = np.random.rand()
        self.w2 = np.random.rand()
        self.w3 = np.random.rand()
        self.b = np.random.rand()
        self.lr = 0.5


    def output(self, x1, x2, x3):
        if self.non_linear:
            return self.sigmoid(x1*self.w1 + x2*self.w2 + x3*self.w3 + self.b)
        else:
            return x1*self.w1 + x2*self.w2 + x3*self.w3 + self.b
        
    def output1(self, x1, x2):
        if self.non_linear:
            return self.sigmoid(x1*self.w1 + x2*self.w2 + self.b)
        else:
            return x1*self.w1 + x2*self.w2 + self.b

        
    def expected_output(self, y):
        if self.non_linear:
            return self.sigmoid(y)
        else:
            return y

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def train(self, df):
        if self.non_linear:
            self.train_non_linear(df)
        else:
            self.train_linear(df)
    
    def train_linear(self, df):
        for row in df.values:
            y = self.expected_output(row[3])
            y_pred = self.output(row[0], row[1], row[2])
            self.w1 += self.lr*(y - y_pred)*row[0]
            self.w2 += self.lr*(y - y_pred)*row[1]
            self.w3 += self.lr*(y - y_pred)*row[2]
            self.b += self.lr*(y - y_pred)

    def train_non_linear(self, df):
         for row in df.values:
            y = self.expected_output(row[3])
            y_pred = self.output(row[0], row[1], row[2])
            self.w1 += self.lr*(y - y_pred)*row[0]*self.sigmoid_derivative(y_pred)
            self.w2 += self.lr*(y - y_pred)*row[1]*self.sigmoid_derivative(y_pred)
            self.w3 += self.lr*(y - y_pred)*row[2]*self.sigmoid_derivative(y_pred)
            self.b += self.lr*(y - y_pred)*self.sigmoid_derivative(y_pred)

    def train1(self, df):
        for row in df.values:
            y = self.expected_output(row[2])  # Aquí usamos x3
            y_pred = self.output1(row[0], row[1])  # Aquí omitimos x3
            if y_pred != y:
                self.w1 += self.lr*(y - y_pred)*row[0]
                self.w2 += self.lr*(y - y_pred)*row[1]
                self.b += self.lr*(y - y_pred)



    def predict(self, df):
        result = pd.DataFrame(columns=['x1', 'x2', 'x3', 'y', 'y_pred'])
        for row in df.values:
            y_pred = row[0]*self.w1 + row[1]*self.w2 + row[2]*self.w3 + self.b
            result.loc[len(result)] = [row[0], row[1], row[2], row[3], y_pred]
        return result
    
    def predict1(self, df):
        result = pd.DataFrame(columns=['x1', 'x2', 'y_pred'])  
        for row in df.values:
            y_pred = row[0] * self.w1 + row[1] * self.w2 + self.b  
            result.loc[len(result)] = [row[0], row[1], y_pred] 
        return result


    def test(self, df):
        for row in df.values:
            print("x1", row[0], " x2:", row[1], " x3:", row[2], " y:", row[3])

    def test1(self, df):
        for row in df.values:
            print("x1:", row[0], " x2:", row[1], " x3:", row[2])


    def get_weights(self):
        return self.w1, self.w2, self.w3, self.b
    
    def set_weights(self, w1, w2, w3, b):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.b = b