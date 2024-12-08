import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


ixus = 'IXUS'
batch_ixus = batched_data[ixus]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_ixus):
	print(f"\nBatch {i+1} for {ixus}:\n")
	ixus_batches = pd.DataFrame(batch)
	batch_dataframes[f'ixus_batch_{i+1}'] = ixus_batches  # Store in dictionary

# The first batch
ixus_batch_1 = batch_dataframes['ixus_batch_1']

# The second batch
ixus_batch_2 = batch_dataframes['ixus_batch_2']

# The third batch
ixus_batch_3 = batch_dataframes['ixus_batch_3']

# The fourth batch
ixus_batch_4 = batch_dataframes['ixus_batch_4']

# The fifth batch
ixus_batch_5 = batch_dataframes['ixus_batch_5']


