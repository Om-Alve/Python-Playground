import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcdefaults()

data = pd.read_csv("amazon.csv", thousands='.')
print(data.shape)
print(data.head())
print(data.describe(include="all"))

data2 = data.remove
