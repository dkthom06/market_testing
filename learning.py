import os
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name = 'TSLA_data.csv'

data = pd.read_csv(file_name, index_col='Date', parse_dates=True)
print(f"Loaded data from {file_name}")
print()

# Calculate the 45-day SMA for the 'Close' column
data['45_day_SMA'] = data['Close'].rolling(window=45).mean()

# Drop unused columns -- ADJUSTED CLOSE needs to be considered vs CLOSE --
data = data.drop(['Open','High','Low','Volume'] , axis=1)

print(data.tail())
print()
print('*********************************************************************************')

plt.plot(data.index, data['Adj Close'])
plt.plot(data.index, data['45_day_SMA'])

plt.xlabel('Year')
plt.ylabel('Price')
plt.title('TSLA Price Graph')
#plt.xticks([2020,2021,2022,2023,2024])
plt.yticks([0,50,100,150,200,250,300,350,400,450],
           ['$0','$50','$100','$150','$200','$250','$300','$350','$400','$450'])

plt.show()