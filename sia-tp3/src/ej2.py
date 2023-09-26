import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import perceptron
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import LeaveOneOut

# Read the CSV file into a DataFrame
df = pd.read_csv('sia-tp3\data\TP3-ej2-conjunto.csv')
_, df_test = train_test_split(df, test_size=0.5, random_state=42)


def run():
    perceptron.Perceptron.non_linear = False
    for i in range(2):
        # Bootstrap Perceptron
        bootstrapping_evaluate()
        # Random Selection Perceptron
        random_selection_evaluate()
        # K-Fold Cross Validation Perceptron
        k_fold_cross_validation_evaluate()
        # Leave One Out Cross Validation Perceptron
        leave_one_out_cross_validation_evaluate()
        perceptron.Perceptron.non_linear = True

def bootstrapping(sample_size, iterations):
    perceptrons = pd.DataFrame(columns=['w1', 'w2', 'w3', 'b'])
    for _ in range(iterations):
        temp_df = df.sample(n=sample_size, random_state=42)
        p = perceptron.Perceptron()
        p.train(temp_df)
        w1, w2, w3, b = p.get_weights()
        perceptrons.loc[len(perceptrons)] = [w1, w2, w3, b]
    p = perceptron.Perceptron()
    p.set_weights(np.mean(perceptrons['w1']), np.mean(perceptrons['w2']), np.mean(perceptrons['w3']), np.mean(perceptrons['b']))
    return p

def random_selection(test_size):
    df_train, df_test = train_test_split(df, test_size=test_size, random_state=42)
    p = perceptron.Perceptron()
    p.train(df_train)
    return p

def k_fold_cross_validation(k):
    perceptrons = pd.DataFrame(columns=['w1', 'w2', 'w3', 'b'])
    kf = KFold(n_splits=k, shuffle=False, random_state=None)  # Use a fixed random_state for reproducibility
    for train_index, test_index in kf.split(df):
        p = perceptron.Perceptron()
        p.train(df.iloc[train_index])
        w1, w2, w3, b = p.get_weights()
        perceptrons.loc[len(perceptrons)] = [w1, w2, w3, b]
    p = perceptron.Perceptron()
    p.set_weights(np.mean(perceptrons['w1']), np.mean(perceptrons['w2']), np.mean(perceptrons['w3']), np.mean(perceptrons['b']))
    return p

def leave_one_out_cross_validation():
    perceptrons = pd.DataFrame(columns=['w1', 'w2', 'w3', 'b'])
    loo = LeaveOneOut()
    for train_index, test_index in loo.split(df):
        p = perceptron.Perceptron()
        p.train(df.iloc[train_index])
        w1, w2, w3, b = p.get_weights()
        perceptrons.loc[len(perceptrons)] = [w1, w2, w3, b]
    p = perceptron.Perceptron()
    p.set_weights(np.mean(perceptrons['w1']), np.mean(perceptrons['w2']), np.mean(perceptrons['w3']), np.mean(perceptrons['b']))
    return p

#Evaluate the performance of the perceptron with MSE(Mean Square Error) and MAE(Mean Absolute Error)
def evaluate(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    mae = mean_absolute_error(actual, predicted)
    return mse, mae

#Plot grapg with two different y-axis for MSE and MAE with shared x-axis
def plot_graph(title, y1, y2, x):
    # Create a figure and axis for the first curve
    fig, ax1 = plt.subplots()
    # Plot the first curve on the left y-axis
    ax1.plot(x, y1, label='MSE', color='b', marker='o', markersize=5)
    # Set labels and title for the left y-axis
    ax1.set_xlabel('X-axis')
    ax1.set_ylabel('MSE-axis', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    # Create a second y-axis (right y-axis) sharing the same x-axis
    ax2 = ax1.twinx()
    # Plot the second curve on the right y-axis
    ax2.plot(x, y2, label='MAE', color='r', linestyle='--', marker='s', markersize=5)
    # Set labels and title for the right y-axis
    ax2.set_ylabel('MAE-axis', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    # Add a legend for both curves
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines = lines1 + lines2
    labels = labels1 + labels2
    ax1.legend(lines, labels, loc='upper left')
    # Show the plot
    plt.title(title)
    plt.grid(True)
    plt.show()

#train the perceptrons with bootstrapping with different sample sizes ranging from 2 to 22 and plot the performance on a graph
def bootstrapping_evaluate():
    evalueations = []
    intervals = [i for i in range(2, 11, 2)]
    for i in intervals:
        p = bootstrapping(i, 10)
        evalueations.append(evaluate(df_test['y'], p.predict(df_test)['y_pred']))
    y1 = [i[0] for i in evalueations]
    y2 = [i[1] for i in evalueations]
    plot_graph("Bootstrapping" ,y1, y2, intervals)

#train the perceptrons with random selection with different test sizes ranging from 0.1 to 0.9 and plot the performance on a graph
def random_selection_evaluate():
    evalueations = []
    intervals = [i/10 for i in range(1, 10)]
    for i in intervals:
        p = random_selection(i)
        evalueations.append(evaluate(df_test['y'], p.predict(df_test)['y_pred']))
    y1 = [i[0] for i in evalueations]
    y2 = [i[1] for i in evalueations]
    plot_graph("Random Selection", y1, y2, intervals)

#train the perceptrons with k-fold cross validation with different k values ranging from 2 to 10 and plot the performance on a graph
def k_fold_cross_validation_evaluate():
    evalueations = []
    intervals = [i for i in range(2, 11, 2)]
    for i in intervals:
        p = k_fold_cross_validation(i)
        evalueations.append(evaluate(df_test['y'], p.predict(df_test)['y_pred']))
    y1 = [i[0] for i in evalueations]
    y2 = [i[1] for i in evalueations]
    plot_graph("K-Fold Cross Validation", y1, y2, intervals)

#train the perceptrons with leave one out cross validation and plot the performance on a graph
def leave_one_out_cross_validation_evaluate():
    p = leave_one_out_cross_validation()
    mse, mae = evaluate(df_test['y'], p.predict(df_test)['y_pred'])
    plot_graph("Leave One Out Cross Validation", [mse], [mae], [1])

def mean_squared_error(actual, predicted):
    return np.mean((actual - predicted)**2)

def mean_absolute_error(actual, predicted):
    return np.mean(np.abs(actual - predicted))
    
run()