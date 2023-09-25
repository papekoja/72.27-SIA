import numpy as np

class Perceptron:
    
    def __init__(self):
        self.w1 = np.random.rand()
        self.w2 = np.random.rand()
        self.w3 = np.random.rand()
        self.b = np.random.rand()
        self.lr = 0.1
        
    def train(self, df):
        for row in df.values:
            y_pred = row[0]*self.w1 + row[1]*self.w2 + row[2]*self.w3 + self.b
            if y_pred != row[3]:
                self.w1 += self.lr*(row[3] - y_pred)*row[0]
                self.w2 += self.lr*(row[3] - y_pred)*row[1]
                self.w3 += self.lr*(row[3] - y_pred)*row[2]
                self.b += self.lr*(row[3] - y_pred)
            

    def predict(self, df):
        for row in df.values:
            y_pred = row[0]*self.w1 + row[1]*self.w2 + row[2]*self.w3 + self.b
            print("x1", row[0], " x2:", row[1], " x3:", row[2], " y:", row[3], " y_pred:", y_pred)

    def test(self, df):
        for row in df.values:
            print("x1", row[0], " x2:", row[1], " x3:", row[2], " y:", row[3])

    def get_weights(self):
        return self.w1, self.w2, self.w3, self.b