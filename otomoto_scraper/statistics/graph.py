import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv('test.csv')

# Extract the numerical value from the km field and convert it to int
df['km'] = df['km'].str.extract('(\d+)').astype(int)

# Get the first word of the car name
df['carname'] = df['carname'].str.split().str[0]

# Group the data by car name and calculate the average kilometers
average_km_by_carname = df.groupby('carname')['km'].mean()

average_km_by_carname.plot(kind='bar')
plt.title("Average Kilometers by carname")
plt.xlabel("Marka samochodów")
plt.ylabel("Średnia ilość kilometrów")
plt.show()