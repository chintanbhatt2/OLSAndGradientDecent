import os 
import pandas as pd


def main():
    csv = pd.read_csv("/home/cb/Desktop/Programming/Python/CS422/Assignment3/dataset/macroeconomics/raw/10YearInflation.csv")
    newHeader = ["Year", "Month", "Day", "T10YIE"]
    data = []
    for x in csv["DATE"]:
        data.append([x[0:4], x[5:7], x[8:10]])
    for i, x in enumerate(csv["T10YIE"]):
        data[i].append(x)
    df = pd.DataFrame(data)
    df.to_csv("/home/cb/Desktop/Programming/Python/CS422/Assignment3/dataset/macroeconomics/formatted/10YearInflation.csv", header=newHeader, index=False)

if __name__ == "__main__":
    main()
else:
    print("Do not call this file from other files!")
    exit()