import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

class OLS:
    csv1 = None
    csv2 = None
    xAxis = None
    xLabel = None
    yLabel = None
    yAxis = None
    fitModel = None
    dataSet1 = []
    dataSet2 = []


    def readFile(self, path1:str, path2:str):
        self.csv1 = pd.read_csv(path1, index_col=False)
        self.csv2 = pd.read_csv(path2, index_col=False)
        
    def __init__(self) -> None:
        pass
    def __eq__(self, o: object) -> bool:
        pass


    def setUpAxes(self, x:str, y:str):
        self.xAxis = self.csv1[x]
        self.xLabel = x
        self.yAxis = self.csv2[y]
        self.yLabel = y
        

    def classify(self):
        model = sm.OLS(self.xAxis, self.yAxis);
        self.fitModel = model.fit()
        print(self.fitModel.params)
        

    def graph(self):
        plt.scatter(x=self.xAxis, y=self.YAxis)
        print(self.fitModel.predict())
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.show()
