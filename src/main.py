import matplotlib.pyplot as plt
from OLS import OLS
from LRGD import LRGD


def main():
    ols = OLS()
    ols.readFile("/home/cb/Desktop/Programming/Python/CS422/Assignment3/dataset/titanic.csv")
    ols.setUpAxes("Fare", "Survived")
    print(ols.csv)
    print(ols.yAxis)
    print(ols.xAxis)
    

if __name__ == "__main__":
    main()
else:
    print("Main not selected as main file!")
    exit()