import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class LRGD:
    csv = None
    def __init__(self, path) -> None:
        csv = pd.read_csv(path)
    def __eq__(self, o: object) -> bool:
        pass
    def print(self) -> None:
        pass