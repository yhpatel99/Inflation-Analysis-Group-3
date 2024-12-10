import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'global_inflation_data.csv'  
inflation_data = pd.read_csv(data_path)

# Countries of interest and years to extract (last 5 years: 2019-2023)
countries = ['Argentina', 'Zimbabwe', 'Sudan', 'United States']
years = ['2019', '2020', '2021', '2022', '2023']

# Filter data for the selected countries and years
filtered_data = inflation_data[inflation_data['country_name'].isin(countries)]
filtered_data = filtered_data[['country_name'] + years]

# Melt the data to make it suitable for plotting
filtered_data_melted = filtered_data.melt(id_vars='country_name', 
                                          var_name='Year', 
                                          value_name='Inflation Rate')

# Convert 'Year' to numeric for proper sorting
filtered_data_melted['Year'] = pd.to_numeric(filtered_data_melted['Year'])

# Plot the data
plt.figure(figsize=(12, 8))
sns.lineplot(data=filtered_data_melted, x='Year', y='Inflation Rate', hue='country_name', marker='o')

# Customize the plot
plt.title('Inflation Rates (2019-2023): Argentina, Zimbabwe, Sudan, and USA', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Inflation Rate (%)', fontsize=12)
plt.legend(title='Country', fontsize=10)
plt.xticks([2019, 2020, 2021, 2022, 2023])  # Set proper year labels without decimals
plt.grid(visible=True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
