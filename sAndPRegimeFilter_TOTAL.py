import os
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Set the start and end date
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=1000)

print('End Date: ' + str(end_date))
print('Start Date: ' + str(start_date))

# Set the ticker
ticker = '^GSPC'

# Set the file name
file_name = ticker + '1000day' +'_data.csv'

# Check if the data file already exists
if not os.path.exists(file_name):
    # If not, download the data
    data = yf.download(ticker, start_date, end_date)
    # Reduce to the date and the close price
    # np_data = np.array(data[:][0] + data[:][4])

    # Save the data to a CSV file
    data.to_csv(file_name)
    print(f"Downloaded and saved data to {file_name}")
else:
    # If it does, read the data from the CSV file
    data = pd.read_csv(file_name, index_col='Date', parse_dates=True)
    print(f"Loaded data from {file_name}")

# Print 5 rows
# print(data.tail())
    
# Calculate the 45-day SMA for the 'Close' column
# data['45_day_SMA'] = data['Adj Close'].rolling(window=45).mean()
data['45_day_SMA'] = data['Adj Close'].rolling(window=45, min_periods=1).mean()

# Drop unused columns -- ADJUSTED CLOSE needs to be considered vs CLOSE --
data = data.drop(['Open','High','Low','Volume', 'Close'] , axis=1)

print(data)
print()
print('*********************************************************************************')

plt.plot(data.index, data['Adj Close'])
plt.plot(data.index, data['45_day_SMA'])

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('S&P 500 Price Graph')
#plt.xticks([2020,2021,2022,2023,2024])
# plt.yticks([0,50,100,150,200,250,300,350,400,450],
#           ['$0','$50','$100','$150','$200','$250','$300','$350','$400','$450'])

plt.show()

regimeFilter = data['Adj Close'].tail(1).values[0] - data['45_day_SMA'].tail(1).values[0]

print('45_day_SMA:')
print(data['45_day_SMA'].tail(1).values[0])
print()
print('Adj Close')
print(data['Adj Close'].tail(1).values[0])

print('********************************************************************************')
if regimeFilter > 0:
    print('BUY BUY BUY')
else:
    print('GET OUT!')
#print('Result: ' + str(regimeFilter))
print('********************************************************************************')