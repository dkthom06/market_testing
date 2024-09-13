import os
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Set the start and end date
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=200)


print('End Date: ' + str(end_date))
print('Start Date: ' + str(start_date))

# Set the ticker
ticker = '^GSPC'

# Set the file name
file_name = ticker + '_data.csv'

# Get the day it was last modified

# Check if the data file already exists
if not os.path.exists(file_name):
    # If not, download the data
    data = yf.download(ticker, start_date, end_date)
    
    # Save the data to a CSV file
    data.to_csv(file_name)
    print(f"Downloaded and saved data to {file_name}")

else:
    # If it does, read the data from the CSV file
    file_modification_time = os.path.getmtime(file_name)
    last_modified_date = datetime.date.fromtimestamp(file_modification_time)
    today = datetime.date.today()
    print('Last Modified Date: ' + str(last_modified_date))
    if last_modified_date < today:
        print("Data is not up to date. Downloading the latest data.")
        data = yf.download(ticker, start_date, end_date)
        # Save the data to a CSV file
        data.to_csv(file_name)
        print(f"Downloaded and saved data to {file_name}")
    else:
        data = pd.read_csv(file_name, index_col='Date', parse_dates=True)
        print(f"Loaded data from {file_name}")


# Print 5 rows
# print(data.tail())
    
# Calculate the 45-day SMA for the 'Close' column
# data['45_day_SMA'] = data['Adj Close'].rolling(window=45).mean()
data['45_day_SMA'] = data['Adj Close'].rolling(window=45, min_periods=1).mean()

# Drop unused columns -- ADJUSTED CLOSE needs to be considered vs CLOSE --
data = data.drop(['Open','High','Low','Volume', 'Close'] , axis=1)

# Is the 45 SMA regime filter active?
last_close = data['Adj Close'][-1]
last_45_day_SMA = data['45_day_SMA'][-1]
filter_status = last_close > last_45_day_SMA  #True: active, False: not active
filter_result = 'Bull' if filter_status else 'Bear'

# Print Results
print()
print()
if filter_status:
    print(f"{ticker} is currently in a {filter_result} regime. BUY BUY BUY")
else:
    print(f"{ticker} is currently not in a {filter_result} regime. SELL SELL SELL")
print()

# Plot the Adj Close and 45-day SMA prices over time
last_50_days = data[-50:]

plt.plot(last_50_days.index, last_50_days['Adj Close'])
plt.plot(last_50_days.index, last_50_days['45_day_SMA'])

plt.xlabel('Date')
plt.ylabel('Price')
plt.title(ticker + ' Price Graph')
# plt.xticks([2020,2021,2022,2023,2024])
# plt.yticks([0,50,100,150,200,250,300,350,400,450],
#           ['$0','$50','$100','$150','$200','$250','$300','$350','$400','$450'])

plt.show()