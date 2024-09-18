# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import requests
import os
from io import StringIO
import numpy as np

# URL of the NASA GISTEMP data file
data_url = 'https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv'

# Fetch the data with headers
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(data_url, headers=headers)

if response.status_code == 200:
    data = response.content.decode('utf-8', errors='ignore')
    # Read the CSV data into pandas
    df = pd.read_csv(StringIO(data), skiprows=1)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Data cleaning and processing
df = df.iloc[:-1, :-1]  # Drop the last row and unnecessary columns

# Melt the DataFrame to have 'Year' and 'Month' columns
df_melted = df.melt(id_vars=['Year'], var_name='Month', value_name='Temperature')

# Replace '***' with NaN and drop missing values
df_melted['Temperature'] = df_melted['Temperature'].replace('***', pd.NA)
df_melted.dropna(inplace=True)

# Convert Temperature to float
df_melted['Temperature'] = df_melted['Temperature'].astype(float)

# Calculate annual average temperatures
annual_temps = df_melted.groupby('Year')['Temperature'].mean().reset_index()

# Create the 'charts' directory if it doesn't exist
if not os.path.exists('charts'):
    os.makedirs('charts')

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(annual_temps['Year'], annual_temps['Temperature'], marker='o', linestyle='-', label='Annual Average')
plt.title('Global Average Temperature Anomalies (°C) from 1923 to 2023')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid(True)

# Calculate and plot the trend line
z = np.polyfit(annual_temps['Year'], annual_temps['Temperature'], 1)
p = np.poly1d(z)
plt.plot(annual_temps['Year'], p(annual_temps['Year']), "r--", label='Trend Line')
plt.legend()

plt.tight_layout()

# Save the figure
plt.savefig('charts/global_temperature_trend.png')

# Show the plot
plt.show()