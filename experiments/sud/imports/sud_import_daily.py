# This file handles the APIs for the model

# Libraries
import yfinance as yfin
import pandas as pd  # Build dataframe

# We will need to identify the stocks and iterate through them to build our training set
# This is a list of ETFs that we will treat as the stock tickers we will use for training
training_stocks = ['NOBL', 'VYMI', 'PEY', 'XLE', 'VYM', 'HDV', 'SCHD',
				   'DGRO', 'HDV', 'JNK', 'HYG', 'SCHD', 'IXUS', 'DJIA',
				   'LIT', 'SPHD', 'ISCF', 'HSCZ', 'HDEF', 'PCY', 'BNDX',
				   'SMX', 'HEFA', 'IYK', 'OIL', 'XLF', 'VFH', 'KRE',
				   'IYF', 'FNCL', 'QQQ', 'SPY']


# Daily data (Separate files for week and month) ___________________________

# The API we will use for daily values, make the ticker symbol replaceable so we can iterate through the stock list
def daily_ticker(stock):
	daily_api = yfin.Ticker(f"{stock}")
	return daily_api


# Use the variable returned from the previous function
# Get the data from the API
def daily_source(daily_api):
	market_response = daily_api.history(period='5y')
	return daily_values(market_response)


# Build our initial list with the values we want from the data
def daily_values(market_response):
	value_day = market_response.reset_index()  # Ensure 'Date' is a column, not an index
	return value_day


# Slice the list such that we only take the last 500 values from each stock
def indexed_list(value_day):
	value_day_index = value_day[-500:]  # Slicing the list
	return value_day_index


# Take the sliced list and build a dataframe for each set of values
def daily_frame(value_day_index):
	daily_training_frame = pd.DataFrame(value_day_index, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
	return daily_training_frame


# Define the operation of the file
def main():
	data_frames = {}  # Create a dictionary to store the dataframes
	for stock in training_stocks:  # Iterate through the stock list
		print(f"\nProcessing {stock}...\n")
		daily_api = daily_ticker(stock)  # Format the API
		value_day = daily_source(daily_api)  # Get the data from the API
		value_day_index = indexed_list(value_day)  # Slice the data
		daily_training_frame = daily_frame(value_day_index)  # Get our dataframes
		data_frames[stock] = daily_training_frame  # Store the frames in the dictionary
	return data_frames  # Return the dictionary


if __name__ == "__main__":
	all_frames = main()  # Store the returned value in a variable
