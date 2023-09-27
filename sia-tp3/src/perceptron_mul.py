import numpy as np

class MultilayerPerceptron:
    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Inicializar los pesos y sesgos de la capa oculta y de salida
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def train(self, X, y, epochs):
        for _ in range(epochs):
            # Capa de entrada a capa oculta
            hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
            hidden_output = self.sigmoid(hidden_input)
            
            # Capa oculta a capa de salida
            output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            output = self.sigmoid(output_input)
            
            # Calcular el error
            error = y - output
            
            # Retropropagación y ajuste de pesos
            d_output = error * self.sigmoid_derivative(output)
            error_hidden = d_output.dot(self.weights_hidden_output.T)
            d_hidden = error_hidden * self.sigmoid_derivative(hidden_output)
            
            self.weights_hidden_output += hidden_output.T.dot(d_output) * self.learning_rate
            self.bias_output += np.sum(d_output, axis=0, keepdims=True) * self.learning_rate
            self.weights_input_hidden += X.T.dot(d_hidden) * self.learning_rate
            self.bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * self.learning_rate
    
    def predict(self, X):
        # Capa de entrada a capa oculta
        hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        
        # Capa oculta a capa de salida
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        output = self.sigmoid(output_input)
        
        return output
    
    def train_with_gradient_descent(self, X, y, epochs):
        for _ in range(epochs):
            # Propagación hacia adelante (Forward Pass)
            hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
            hidden_output = self.sigmoid(hidden_input)
            output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            output = self.sigmoid(output_input)

            # Cálculo de la pérdida
            loss = np.mean(0.5 * (y - output) ** 2)

            # Retropropagación y ajuste de pesos
            d_output = (y - output) * self.sigmoid_derivative(output)
            error_hidden = d_output.dot(self.weights_hidden_output.T)
            d_hidden = error_hidden * self.sigmoid_derivative(hidden_output)

            self.weights_hidden_output += hidden_output.T.dot(d_output) * self.learning_rate
            self.bias_output += np.sum(d_output, axis=0, keepdims=True) * self.learning_rate
            self.weights_input_hidden += X.T.dot(d_hidden) * self.learning_rate
            self.bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * self.learning_rate

            #if _ % 100 == 0:
            #    print(f'Epoch {_}, Loss: {loss}')


    def train_with_adam(self, X, y, epochs):
        beta1 = 0.9  # Coeficiente de decaimiento para el primer momento
        beta2 = 0.999  # Coeficiente de decaimiento para el segundo momento
        epsilon = 1e-8  # Pequeña constante para evitar la división por cero
        
        m_t_wih = np.zeros_like(self.weights_input_hidden)
        v_t_wih = np.zeros_like(self.weights_input_hidden)
        m_t_bh = np.zeros_like(self.bias_hidden)
        v_t_bh = np.zeros_like(self.bias_hidden)
        
        m_t_who = np.zeros_like(self.weights_hidden_output)
        v_t_who = np.zeros_like(self.weights_hidden_output)
        m_t_bo = np.zeros_like(self.bias_output)
        v_t_bo = np.zeros_like(self.bias_output)
        
        t = 0  # Paso de tiempo
        
        for _ in range(epochs):
            for i in range(len(X)):
                t += 1
                
                # Propagación hacia adelante (Forward Pass)
                hidden_input = np.dot(X[i], self.weights_input_hidden) + self.bias_hidden
                hidden_output = self.sigmoid(hidden_input)
                output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
                output = self.sigmoid(output_input)

                # Cálculo de la pérdida
                loss = np.mean(0.5 * (y[i] - output) ** 2)

                # Retropropagación y ajuste de pesos
                d_output = (y[i] - output) * self.sigmoid_derivative(output)
                error_hidden = d_output.dot(self.weights_hidden_output.T)
                d_hidden = error_hidden * self.sigmoid_derivative(hidden_output)

                # Actualización de los momentos
                m_t_wih = beta1 * m_t_wih + (1 - beta1) * d_hidden
                v_t_wih = beta2 * v_t_wih + (1 - beta2) * (d_hidden ** 2)
                m_t_bh = beta1 * m_t_bh + (1 - beta1) * d_hidden
                v_t_bh = beta2 * v_t_bh + (1 - beta2) * (d_hidden ** 2)
                
                m_t_who = beta1 * m_t_who + (1 - beta1) * d_output
                v_t_who = beta2 * v_t_who + (1 - beta2) * (d_output ** 2)
                m_t_bo = beta1 * m_t_bo + (1 - beta1) * d_output
                v_t_bo = beta2 * v_t_bo + (1 - beta2) * (d_output ** 2)

                # Corrección de sesgo
                m_t_wih_hat = m_t_wih / (1 - beta1 ** t)
                v_t_wih_hat = v_t_wih / (1 - beta2 ** t)
                m_t_bh_hat = m_t_bh / (1 - beta1 ** t)
                v_t_bh_hat = v_t_bh / (1 - beta2 ** t)
                
                m_t_who_hat = m_t_who / (1 - beta1 ** t)
                v_t_who_hat = v_t_who / (1 - beta2 ** t)
                m_t_bo_hat = m_t_bo / (1 - beta1 ** t)
                v_t_bo_hat = v_t_bo / (1 - beta2 ** t)

                # Actualización de pesos y sesgos
                self.weights_input_hidden += self.learning_rate * m_t_wih_hat / (np.sqrt(v_t_wih_hat) + epsilon)
                self.bias_hidden += self.learning_rate * m_t_bh_hat / (np.sqrt(v_t_bh_hat) + epsilon)
                
                self.weights_hidden_output += self.learning_rate * m_t_who_hat / (np.sqrt(v_t_who_hat) + epsilon)
                self.bias_output += self.learning_rate * m_t_bo_hat / (np.sqrt(v_t_bo_hat) + epsilon)

                #if _ % 100 == 0:
                #    print(f'Epoch {_}, Loss: {loss}')

    

