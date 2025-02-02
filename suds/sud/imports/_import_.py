import os
import sys
import pandas as pd
import yfinance as yfin

# Add the necessary paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))

# Pull in the training stocks
training_stocks = ['NOBL', 'VYMI', 'PEY', 'XLE', 'VYM', 'HDV', 'GLNCY',
				   'DGRO', 'HDV', 'JNK', 'HYG', 'SCHD', 'IXUS', 'DJIA',
				   'LIT', 'SPHD', 'ISCF', 'HSCZ', 'HDEF', 'PCY', 'BNDX',
				   'SMX', 'HEFA', 'IYK', 'USOI', 'XLF', 'VFH', 'KRE',
				   'IYF', 'FNCL', 'QQQ', 'SPY', 'VTI', 'ITOT', 'XLK',
				   'XLY', 'XLV', 'EEM', 'VEU', 'VB']

# Function to fetch and process stock data
def fetch_and_process_data(stock):
	daily_api = yfin.Ticker(f"{stock}")
	market_response = daily_api.history(period='5y')
	value_day = market_response.reset_index()
	value_day_index = value_day[-500:]
	daily_training_frame = pd.DataFrame(value_day_index, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
	return daily_training_frame

# Function to create old_batching_files of 100 for each stock
def create_batches(data_frames, batch_size=100, num_batches=5):
	batched_data = {}
	for stock, df in data_frames.items():
		# Create old_batching_files
		batches = [df.iloc[i*batch_size:(i+1)*batch_size] for i in range(num_batches)]
		# Ensure each batch has the correct number of rows
		batches = [batch if len(batch) == batch_size else pd.DataFrame(columns=df.columns) for batch in batches]
		# Convert to numpy arrays
		batched_data[stock] = [batch.to_numpy() for batch in batches]
	return batched_data

# Main function to process all stocks and create old_batching_files
def main():
	data_frames = {}
	for stock in training_stocks:
		print(f"\nProcessing {stock}...\n")
		daily_training_frame = fetch_and_process_data(stock)
		data_frames[stock] = daily_training_frame

	batched_data = create_batches(data_frames)
	return batched_data

if __name__ == "__main__":
	all_batches = main()
	print(all_batches)  # Optional: Print to verify the output
