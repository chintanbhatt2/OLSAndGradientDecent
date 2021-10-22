import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd
from pandas.core.construction import array
from scipy.sparse.construct import random
import statsmodels.api as sm
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as lm


#replace sourcePath
sourcePath = "C:/Users/cb/Desktop/School/CS422/OLSAndGradientDecent"

#scrapping the classes for now in favor of getting it working
def main():
    #OLS
    data = pd.read_csv(sourcePath + "/dataset/winequality-red.csv")
    Y = data["quality"]
    X = data[["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol"]]
    X = sm.add_constant(X)
    xTraining, xTest, yTraining, yTest = ms.train_test_split(X, Y, test_size=0.2, random_state=3)
    model = sm.OLS(yTraining, xTraining)
    model_results = model.fit()
    print(model_results.summary())
    print(round(data.corr(), 2))

    #Gradient decent
    learningRate = 0.001
    iterations = 1000
    m = 0
    c = 0
    n = len(X)
    xValues = X.values
    xValues = list(map(list, zip(*xValues)))
    xValues = np.array(xValues)
    yValues = np.array(Y.values)
    regDict = [None] * 12
    np.delete(xValues, 0)
    for col in range(X.columns.size):
        m = 0
        c = 0
        for i in range(iterations):
            yPrediction = m * xValues[col] + c
            Dm = sum(xValues[col] * (yValues - yPrediction))
            Dc = sum(yValues- yPrediction)
            Dm *=(-2/n)
            Dc *=(-2/n)

            m = m - learningRate * Dm 
            c = c - learningRate * Dc
        regDict[col] = [m, c]

        r2 = []

    m = mean(yValues)
    for i, x in enumerate(regDict):
        estimatedValues = x[0]*xValues[i]+x[1]
        estimated_Mean = sum(pow(estimatedValues-m, 2))
        mean_mean = sum(pow(2, yValues - m))

        r2 = estimated_Mean / mean_mean
        try:
            print(X.columns[i+1], r2)
        except:
            pass
    
    

if __name__ == "__main__":
    main()
else:
    print("Main not selected as main file!")
    exit()