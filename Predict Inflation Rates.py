'''Predicting next 5 years of inflation rate for Argentina, Zimbabwe, and Sudan using Random Forest Regressor'''
# Importing libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('global_inflation_data.csv')

# Extract relevant data
countries = ['Sudan', 'Zimbabwe', 'Argentina']
filtered_data = data[data['country_name'].isin(countries)]

# Prepare the data
years = np.array([int(year) for year in data.columns[2:]])
pred_years = np.array([2025, 2026, 2027, 2028, 2029])

predictions = {}

for country in countries:
    country_data = filtered_data[filtered_data['country_name'] == country].iloc[0, 2:].dropna()
    X = years[:len(country_data)].reshape(-1, 1)
    y = country_data.values
    
    # Create lagged features
    lagged_features = np.hstack([np.roll(y, shift)[:, np.newaxis] for shift in range(1, 6)])
    lagged_features = lagged_features[5:]  # Remove the first 5 rows with NaN values
    X = X[5:]  # Remove the first 5 rows to match the lagged features
    y = y[5:]
    
    # Combine years and lagged features
    X_combined = np.hstack([X, lagged_features])
    


    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_combined, y)
    
    # Prepare future data for prediction
    future_lagged_features = []
    for year in pred_years:
        future_lagged_features.append([year] + list(y[-5:]))
        y = np.append(y, model.predict(np.array([[year] + list(y[-5:])])))

    future_lagged_features = np.array(future_lagged_features)
    
    # Predict future values
    future_inflation = model.predict(future_lagged_features)
    predictions[country] = future_inflation


# Display the predictions
for country, future_inflation in predictions.items():
    print(f"Predicted inflation rates for {country} for the next 5 years:")
    for year, rate in zip(pred_years, future_inflation):
        print(f"{year}: {rate:.2f}%")

# Plot the predictions alongside the historical data
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = filtered_data[filtered_data['country_name'] == country].iloc[0, 2:].dropna()
    recent_years = years[:len(country_data)]
    recent_data = country_data[recent_years >= 2019]
    recent_years = recent_years[recent_years >= 2019]
    plt.plot(recent_years, recent_data, label=country)
    plt.plot(pred_years, predictions[country], linestyle='--', label=f"{country} Prediction", color=plt.gca().lines[-1].get_color())


plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.title('Inflation Rate Predictions')
plt.legend()
plt.grid(True)
plt.xlim(2019, 2029)
plt.xticks(range(2019, 2030))
plt.show()
