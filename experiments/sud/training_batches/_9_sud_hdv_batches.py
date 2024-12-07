import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


hdv = 'HDV'
batch_hdv = batched_data[hdv]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_hdv):
	print(f"\nBatch {i+1} for {hdv}:\n")
	hdv_batches = pd.DataFrame(batch)
	batch_dataframes[f'hdv_batch_{i+1}'] = hdv_batches  # Store in dictionary

# The first batch
hdv_batch_1 = batch_dataframes['hdv_batch_1']

# The second batch
hdv_batch_2 = batch_dataframes['hdv_batch_2']

# The third batch
hdv_batch_3 = batch_dataframes['hdv_batch_3']

# The fourth batch
hdv_batch_4 = batch_dataframes['hdv_batch_4']

# The fifth batch
hdv_batch_5 = batch_dataframes['hdv_batch_5']


