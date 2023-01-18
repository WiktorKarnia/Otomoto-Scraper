import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')
df["fuel_type"] = df["fuel_type"].replace("Petrol","Benzyna")
df["fuel_type"] = df["fuel_type"].replace("Hybrid","Hybryda")
df["fuel_type"] = df["fuel_type"].replace(r'\d+',np.nan,regex=True)
df.dropna(subset=["fuel_type"], inplace=True)
counts = df['fuel_type'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.show()