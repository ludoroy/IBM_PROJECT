import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
data = pd.read_csv('preprocessed_data.csv')
data
#Data Description
descriptive_stats = data.describe()
print(descriptive_stats)
#Histogram
plt.hist(data['PJM_Load_MW'], bins=20)
plt.xlabel('Energy Consumption (MW)')
plt.ylabel('Frequency')
plt.title('Histogram of Energy Consumption')
plt.show()
#Box Plot
sns.boxplot(data=data, y='PJM_Load_MW')
plt.ylabel('Energy Consumption (MW)')
plt.title('Box Plot of Energy Consumption')
plt.show()
#Correlation Heatmap
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
#Scatter Plot
plt.scatter(data['PJMW_MW'], data['PJM_Load_MW'])
plt.xlabel('PJMW_MW')
plt.ylabel('PJM_Load_MW')
plt.title('Scatter Plot of Energy Consumption vs. PJMW_MW')
plt.show()
