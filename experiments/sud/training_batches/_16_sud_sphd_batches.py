import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


sphd = 'SPHD'
batch_sphd = batched_data[sphd]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_sphd):
	print(f"\nBatch {i+1} for {sphd}:\n")
	sphd_batches = pd.DataFrame(batch)
	batch_dataframes[f'sphd_batch_{i+1}'] = sphd_batches  # Store in dictionary

# The first batch
sphd_batch_1 = batch_dataframes['sphd_batch_1']

# The second batch
sphd_batch_2 = batch_dataframes['sphd_batch_2']

# The third batch
sphd_batch_3 = batch_dataframes['sphd_batch_3']

# The fourth batch
sphd_batch_4 = batch_dataframes['sphd_batch_4']

# The fifth batch
sphd_batch_5 = batch_dataframes['sphd_batch_5']


