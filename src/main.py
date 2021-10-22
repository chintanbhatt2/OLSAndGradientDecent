import matplotlib.pyplot as plt
from OLS import OLS
from LRGD import LRGD


def main():
    ols = OLS()
    ols.readFile("/home/cb/Desktop/Programming/Python/CS422/Assignment3/dataset/macroeconomics/formatted/CPI.csv", "/home/cb/Desktop/Programming/Python/CS422/Assignment3/dataset/macroeconomics/formatted/10YearInflation.csv")
    print(ols.csv1)
    print(ols.csv2)
    ols.setUpAxes("CPI", "T10YIE")
    ols.classify()
    ols.graph()
    
    

if __name__ == "__main__":
    main()
else:
    print("Main not selected as main file!")
    exit()