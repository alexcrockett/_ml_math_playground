# This file handles the APIs for the model

# Libraries
# import requests  # Handle API
import yfinance as yfin
import pandas as pd  # Build dataframe

# We will need to identify the stocks and iterate through them to build our training set
# This is a list of ETFs that we will treat as the stock tickers we will use for training
training_stocks = ['NOBL', 'VYMI', 'PEY', 'XLE', 'VYM', 'HDV', 'SCHD',
				   'DGRO', 'VYM', 'HDV', 'JNK', 'HYG', 'SCHD', 'IXUS',
				   'LIT', 'SPHD', 'ISCF', 'HSCZ', 'HDEF', 'PCY', 'BNDX']

# Daily data (Separate files for week and month) ___________________________

# The API we will use for daily values, make the ticker symbol replaceable so we can iterate through the stock list
# Notice the argument for the function is the variable we've placed in the URL string
def daily_ticker(stock):
	daily_api = yfin.Ticker(f"{stock}")
	# daily_api_x = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey=<key here>'
	return daily_api

# Use the variable returned from the previous function
# Get the data from the API
def daily_source(daily_api):
	market_response = daily_api.history(period='5y')
	# -----------------------------------------------------------
	# The code below this line can be used with the alpha vantage api
	# market_response_x = requests.get(daily_api)  # Get the data (API version)
	# data = market_response.json()  # Define the data as json formatted
	# daily_data = data["Time Series (Daily)"]  # Indicate what part of the data we want
	# -----------------------------------------------------------
	return daily_values(market_response)  # Return the data

# Build our initial list with the values we want from the data
def daily_values(market_response):
	value_day = pd.DataFrame(market_response)
	# -----------------------------------------------------------
	# value_day = []  # Create an empty list to populate
	# for date, values in daily_data.items():  # For loop to iterate through the values
		# daily_open = float(values['1. open'])
		# daily_high = float(values['2. high'])
		# daily_low = float(values['3. low'])
		# daily_close = float(values['4. close'])
		# daily_volume = float(values['5. volume'])
		# value_day.append([date, daily_open, daily_high, daily_low, daily_close, daily_volume])  # Add these values to the list
	return value_day

# Slice the list such that we only take the last 300 values from each stock
def indexed_list(value_day):
	value_day_index = value_day[-500:]  # Slicing the list
	return value_day_index

# Take the sliced list and build a dataframe for each set of values
def daily_frame(value_day_index):
	daily_training_frame = pd.DataFrame(value_day_index, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
	return daily_training_frame

# Check the work by printing each frame out in the console
def print_list(daily_training_frame):
	print(daily_training_frame)

# Define the operation of the file
def main():
	data_frames = {}  # Create a dictionary we will store the dataframes in for later access
	for stock in training_stocks:  # Indicate we want to iterate through the list
		print(f"\nProcessing {stock}...\n")
		# Notice the dataflow in the code below!
		daily_api = daily_ticker(stock)  # Format the api
		value_day = daily_source(daily_api)  # Get the data from the API
		value_day_index = indexed_list(value_day)  # Slice the data
		daily_training_frame = daily_frame(value_day_index)  # Get our dataframes
		data_frames[f'daily_frame_{stock}'] = daily_training_frame  # Store the frames in the above defined dictionary
		print_list(daily_training_frame)  # Do the print check

if __name__ == "__main__":
	main()
