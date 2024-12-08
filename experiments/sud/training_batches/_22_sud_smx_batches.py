import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


smx = 'SMX'
batch_smx = batched_data[smx]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_smx):
	print(f"\nBatch {i+1} for {smx}:\n")
	smx_batches = pd.DataFrame(batch)
	batch_dataframes[f'smx_batch_{i+1}'] = smx_batches  # Store in dictionary

# The first batch
smx_batch_1 = batch_dataframes['smx_batch_1']

# The second batch
smx_batch_2 = batch_dataframes['smx_batch_2']

# The third batch
smx_batch_3 = batch_dataframes['smx_batch_3']

# The fourth batch
smx_batch_4 = batch_dataframes['smx_batch_4']

# The fifth batch
smx_batch_5 = batch_dataframes['smx_batch_5']


