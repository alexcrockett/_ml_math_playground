import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

# Call batched data for the given stock
def get_batches(stock_symbol):
	batched_data = _0_process_data.batched_data
	batch_stock = batched_data[stock_symbol]

	# Dictionary to store each batch DataFrame
	batch_dataframes = {}

	for i, batch in enumerate(batch_stock):
		print(f"\nBatch {i+1} for {stock_symbol}:\n")
		stock_batches = pd.DataFrame(batch)
		batch_dataframes[f'spy_batch_{i+1}'] = stock_batches  # Store in dictionary

	return batch_dataframes

# Call and make batches
def main():
	stock_symbol = 'SPY'
	batch_dataframes = get_batches(stock_symbol)

	# Accessing specific batches
	spy_batch_1 = batch_dataframes[f'{stock_symbol.lower()}_batch_1']
	spy_batch_2 = batch_dataframes[f'{stock_symbol.lower()}_batch_2']
	spy_batch_3 = batch_dataframes[f'{stock_symbol.lower()}_batch_3']
	spy_batch_4 = batch_dataframes[f'{stock_symbol.lower()}_batch_4']
	spy_batch_5 = batch_dataframes[f'{stock_symbol.lower()}_batch_5']
	spy_list = [spy_batch_1, spy_batch_2, spy_batch_3, spy_batch_4, spy_batch_5]
	# Print the first batch for demonstration
	# print(spy_batch_1.head())
	return spy_list

if __name__ == "__main__":
	main()
