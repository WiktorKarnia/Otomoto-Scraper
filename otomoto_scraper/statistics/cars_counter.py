import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('test.csv')

# Extract the numerical value from the 'price' column
df['price'] = df['price'].str.extract('(\d+)')

# Convert the 'price' column to a numeric data type
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Get the first word of the 'mark' column
df['carname'] = df['carname'].str.split().str[0].str.lower()

# Count the occurrences of each mark
counts = df['carname'].value_counts()

# Plot the counts as a pie chart
counts.plot(kind='bar', color = 'red', width = 0.5)
plt.show()