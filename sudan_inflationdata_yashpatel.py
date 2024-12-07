import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
global_inflation_data = pd.read_csv('global_inflation_data.csv')

# Filter the data for Sudan
sudan_inflation_data = global_inflation_data[global_inflation_data['country_name'] == 'Sudan']

# Keep only the columns for the years 2019 to 2024
sudan_inflation_data_t = sudan_inflation_data[['2019', '2020', '2021', '2022', '2023', '2024']].transpose().reset_index()
sudan_inflation_data_t.columns = ['Year', 'Inflation Rate']

# Convert 'Year' to integer
sudan_inflation_data_t['Year'] = sudan_inflation_data_t['Year'].astype(int)

# Plotting the line chart
plt.figure(figsize=(12, 7))
sns.lineplot(
    data=sudan_inflation_data_t, 
    x='Year', 
    y='Inflation Rate', 
    marker='o', 
    linewidth=3, 
    color='darkblue'
)

# Highlighting the maximum and minimum inflation rates
max_point = sudan_inflation_data_t.loc[sudan_inflation_data_t['Inflation Rate'].idxmax()]
min_point = sudan_inflation_data_t.loc[sudan_inflation_data_t['Inflation Rate'].idxmin()]

plt.scatter(max_point['Year'], max_point['Inflation Rate'], color='red', s=100, label='Highest Inflation')
plt.scatter(min_point['Year'], min_point['Inflation Rate'], color='green', s=100, label='Lowest Inflation')

# Adding annotations on the right side of the points
plt.text(max_point['Year'] + 0.2, max_point['Inflation Rate'], f"{max_point['Inflation Rate']}%", 
         color='red', fontsize=12, va='center', ha='left')
plt.text(min_point['Year'] + 0.2, min_point['Inflation Rate'], f"{min_point['Inflation Rate']}%", 
         color='green', fontsize=12, va='center', ha='left')

# Adding titles and labels
plt.title('Sudan Annual Inflation Rates (2019-2024)', fontsize=18, weight='bold', color='darkblue')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Inflation Rate (%)', fontsize=14)
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)

# Adjust layout and show plot
plt.tight_layout()
plt.show()


