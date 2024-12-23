import pandas as pd
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))
from sud.sud.imports import sud_import_daily as sud
import _0_process_data

# Pull in the training list
ts = sud.training_stocks

# Call batched data for the given stock
def get_batches(symbol):
	batched_data = _0_process_data.batched_data
	batch_stock = batched_data[symbol]

	# Dictionary to store each batch DataFrame
	batch_dataframes = {}

	for i, batch in enumerate(batch_stock):
		print(f"\nBatch {i+1} for {symbol}:\n")
		# Ensure batch is a DataFrame
		stock_batches = pd.DataFrame(batch)
		batch_dataframes[f'{symbol}_batch_{i+1}'] = stock_batches  # Store in dictionary

	return batch_dataframes

# Call and make old_batching_files
def main():
	all_batches = []
	for symbol in ts:
		batch_dataframes = get_batches(symbol)
		all_batches.append(batch_dataframes)
	return all_batches

if __name__ == "__main__":
	main()
