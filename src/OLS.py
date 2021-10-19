import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class OLS:
    csv = None
    xAxis = None
    yAxis = None


    def readFile(self, path:str):
        self.csv = pd.read_csv(path)
    def __init__(self) -> None:
        pass
    def __eq__(self, o: object) -> bool:
        pass


    def setUpAxes(self, x:str, y:str):
        self.xAxis = self.csv[x]
        self.yAxis = self.csv[y]
