import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


xle = 'XLE'
batch_xle = batched_data[xle]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_xle):
	print(f"\nBatch {i+1} for {xle}:\n")
	xle_batches = pd.DataFrame(batch)
	batch_dataframes[f'xle_batch_{i+1}'] = xle_batches  # Store in dictionary

# The first batch
xle_batch_1 = batch_dataframes['xle_batch_1']

# The second batch
xle_batch_2 = batch_dataframes['xle_batch_2']

# The third batch
xle_batch_3 = batch_dataframes['xle_batch_3']

# The fourth batch
xle_batch_4 = batch_dataframes['xle_batch_4']

# The fifth batch
xle_batch_5 = batch_dataframes['xle_batch_5']


