import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'old_batching_files')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))
from sud.sud._archive.old_batching_files._02_pull_batches import get_training_data

training_data = get_training_data()

# Data ____________________________________________________________________________
def fu(training_data):
	all_batches = {}
	for symbol, batches in training_data.items():
		converted_batches = []
		for i, batch in enumerate(batches):
			print(f"Processing batch {i+1} for symbol {symbol}:")
			print(f"Type of batch: {type(batch)}")
			print(f"Content of batch: {batch}")

			if isinstance(batch, pd.DataFrame):
				converted_batches.append(batch.to_numpy())
			else:
				try:
					batch_df = pd.DataFrame(batch)
					converted_batches.append(batch_df.to_numpy())
				except Exception as e:
					print(f"Error converting batch {i+1} for symbol {symbol}: {e}")

		all_batches[symbol] = converted_batches
	return all_batches

# Call the function and get numpy arrays
all_numpy_batches = fu(training_data)
print(all_numpy_batches)  # Optional: Print to verify the output
