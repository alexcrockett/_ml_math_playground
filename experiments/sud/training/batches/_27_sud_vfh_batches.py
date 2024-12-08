import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


vfh = 'VFH'
batch_vfh = batched_data[vfh]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_vfh):
	print(f"\nBatch {i+1} for {vfh}:\n")
	vfh_batches = pd.DataFrame(batch)
	batch_dataframes[f'vfh_batch_{i+1}'] = vfh_batches  # Store in dictionary

# The first batch
vfh_batch_1 = batch_dataframes['vfh_batch_1']

# The second batch
vfh_batch_2 = batch_dataframes['vfh_batch_2']

# The third batch
vfh_batch_3 = batch_dataframes['vfh_batch_3']

# The fourth batch
vfh_batch_4 = batch_dataframes['vfh_batch_4']

# The fifth batch
vfh_batch_5 = batch_dataframes['vfh_batch_5']


