# This file will compartmentalize the data into training batches
# The file will also create labels for each batch

import numpy as np
import pandas as pd
import sud_import_daily as sud

# Call the main function to get the data frames
all_frames = sud.main()

# Function to create batches of 100 for each stock
def create_batches(data_frames, batch_size=100):
	batched_data = {}
	for stock, df in data_frames.items():
		batches = [df.iloc[i:i + batch_size] for i in range(0, len(df), batch_size)]
		batched_data[stock] = batches
	return batched_data

# Create batches
batched_data = create_batches(all_frames)

# Accessing and printing batches for a specific stock
# It would be nice in a future iteration to automate this step further
# For example
# for stock in sud.training_stocks:
	# stock_symbol = stock

nobl = 'NOBL'  # Replace with the desired stock symbol
batch_nobl = batched_data[nobl]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_nobl):
	print(f"\nBatch {i+1} for {nobl}:\n")
	nobl1 = pd.DataFrame(batch)
	batch_dataframes[f'nobl_batch_{i+1}'] = nobl1  # Store in dictionary
	# print(nobl1)

# Access the first batch DataFrame
print(batch_dataframes['nobl_batch_1'])

# Access the second batch DataFrame
print(batch_dataframes['nobl_batch_2'])




