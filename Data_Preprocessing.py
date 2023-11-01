import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('New_CSV.csv')  
data

# Data Cleaning
data.dropna(inplace=True)  # Drop rows with missing values
data.drop_duplicates(inplace=True)  # Remove duplicate rows, if any

# Data Exploration
print(data.describe())

# Plot a histogram of a specific column (e.g., 'PJM_Load_MW')
plt.hist(data['PJM_Load_MW'], bins=20)
plt.xlabel('Energy Consumption (MW)')
plt.ylabel('Frequency')
plt.title('Histogram of PJM Load MW')
plt.show()

# Load the original CSV file into a DataFrame
original_data = pd.read_csv('New_CSV.csv')  

# Convert the 'Datetime' column to a datetime data type
original_data['Datetime'] = pd.to_datetime(original_data['Datetime'])

# Handle missing values (if any) by filling them with the mean of the column
original_data.fillna(original_data.mean(), inplace=True)

# Scale numerical features using StandardScaler (optional)
scaler = StandardScaler()
numerical_columns = ['PJMW_MW', 'PJME_MW', 'PJM_Load_MW', 'NI_MW', 'FE_MW', 'AEP_MW', 'COMED_MW', 'DEOK_MW', 'DOM_MW', 'DUQ_MW', 'EKPC_MW']
original_data[numerical_columns] = scaler.fit_transform(original_data[numerical_columns])

# Save the preprocessed data to a new CSV file
original_data.to_csv('preprocessed_data.csv', index=False)  

