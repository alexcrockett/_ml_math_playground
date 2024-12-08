import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


usoi = 'USOI'
batch_usoi = batched_data[usoi]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_usoi):
	print(f"\nBatch {i+1} for {usoi}:\n")
	usoi_batches = pd.DataFrame(batch)
	batch_dataframes[f'usoi_batch_{i+1}'] = usoi_batches  # Store in dictionary

# The first batch
usoi_batch_1 = batch_dataframes['usoi_batch_1']

# The second batch
usoi_batch_2 = batch_dataframes['usoi_batch_2']

# The third batch
usoi_batch_3 = batch_dataframes['usoi_batch_3']

# The fourth batch
usoi_batch_4 = batch_dataframes['usoi_batch_4']

# The fifth batch
usoi_batch_5 = batch_dataframes['usoi_batch_5']


