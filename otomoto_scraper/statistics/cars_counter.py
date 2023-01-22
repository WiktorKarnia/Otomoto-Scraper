import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Read the CSV file
df = pd.read_csv('test.csv')

# Extract the numerical value from the 'price' column
df['price'] = df['price'].str.extract('(\d+)')

# Convert the 'price' column to a numeric data type
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Get the first word of the 'mark' column
df['carname'] = df['carname'].str.split().str[0].str.title()

# Create a figure with three subplots
#fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 10))
plt.subplots_adjust(hspace=0.7, wspace=0.5)
# Count the occurrences of each mark
counts = df['carname'].value_counts()

# Plot the counts as a bar chart in the first subplot
counts.plot(kind='bar', color = 'red', width = 0.5, ax=ax1)

# Group the data by mark and calculate the average price for each mark
average_prices = df.groupby('carname')['price'].mean()

# Plot the average prices on a bar chart in the second subplot
average_prices.plot(kind='bar', color = 'red', width = 0.5, ax=ax2)



df["fuel_type"] = df["fuel_type"].replace("Petrol","Benzyna")
df["fuel_type"] = df["fuel_type"].replace("Hybrid","Hybryda")
df["fuel_type"] = df["fuel_type"].replace(r'\d+',np.nan,regex=True)
df.dropna(subset=["fuel_type"], inplace=True)
counts = df['fuel_type'].value_counts()

# Plot the counts as a pie chart in the third subplot
ax3.pie(counts, labels=counts.index, autopct='%1.1f%%')

df['km'] = df['km'].str.replace(" ","")

# Remove the "km" unit from the 'km' column
df['km'] = df['km'].str.replace("km","")

# Convert the 'km' column to a numeric data type
df['km'] = pd.to_numeric(df['km'], errors='coerce')

# Create new categories based on the mileage
df['km'] = np.where(df['km'] == 0, np.nan, df['km'])
df['category'] = pd.cut(df['km'], bins=[0, 50, 10000, 20000, 50000, 100000, 300000, 500000, 10000000], labels=['nowe', '<10 000 KM', '10 000 - 20 000 KM', '20 000 - 50 000 KM', '50 000 - 100 000 KM', '100 000 - 300 000 KM', '300 000 - 500 000 KM', '>500 000 KM'])

# Count the occurrences of each category
counts = df['category'].value_counts()


# Plot the counts as a pie chart in the fourth subplot
ax4.pie(counts, labels=counts.index, autopct='%1.1f%%')

ax1.set_title('Ilość samochodów poszczególnych marek')
ax1.set_xlabel("Marka samochodów")
ax1.set_ylabel("Ilość")
ax2.set_title('Średnia cena samochodów')
ax2.set_xlabel("Marka samochodów")
ax2.set_ylabel("Cena (w tysiącach PLN)")
ax3.set_title('Rozkład samochodów ze względu na rodzaj używanego paliwa')
ax4.set_title('Przebieg dostępnych samochodów')

# Show the plot
plt.show()