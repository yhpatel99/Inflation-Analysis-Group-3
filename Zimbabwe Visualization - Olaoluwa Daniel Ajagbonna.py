import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C:/Users/danie/Downloads/School/Info/global_inflation_data.csv')

# Clean the data
# Drop rows with missing values in the relevant columns
data = data.dropna(subset=['2019', '2020', '2021', '2022', '2023'])

# Convert the relevant columns to numeric, if they are not already
data[['2019', '2020', '2021', '2022', '2023']] = data[['2019', '2020', '2021', '2022', '2023']].apply(pd.to_numeric)

# Extract the inflation data for Zimbabwe between 2019 and 2023
# Assuming the data is in the 197th row and columns AP to AT
inflation_data = data.loc[195, ['2019', '2020', '2021', '2022', '2023']]

# Convert the data to a list of inflation rates
inflation_rates = inflation_data.values.tolist()

# Calculate the average inflation rate
average_inflation_rate = sum(inflation_rates) / len(inflation_rates)
print(f"Average Inflation Rate (2019-2023): {average_inflation_rate:.2f}%")

# Define the years
years = [2019, 2020, 2021, 2022, 2023]

# Plot the inflation data as a bar graph
plt.figure(figsize=(10, 6))
plt.bar(years, inflation_rates, color='b')
plt.title('Inflation Rates in Zimbabwe (2019-2023)')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.grid(True)
plt.show()