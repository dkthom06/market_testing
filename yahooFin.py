import os
import yfinance as yf
import numpy as np
import pandas as pd
import datetime 

# Set the start and end date
start_date = '2020-01-01'
end_date = datetime.date.today()

# Set the ticker
ticker = '^GSPC'

# Set the file name
file_name = ticker + '_data.csv'

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
print(data.tail())