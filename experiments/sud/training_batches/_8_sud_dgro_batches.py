import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


dgro = 'DGRO'
batch_dgro = batched_data[dgro]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_dgro):
	print(f"\nBatch {i+1} for {dgro}:\n")
	dgro_batches = pd.DataFrame(batch)
	batch_dataframes[f'dgro_batch_{i+1}'] = dgro_batches  # Store in dictionary

# The first batch
dgro_batch_1 = batch_dataframes['dgro_batch_1']

# The second batch
dgro_batch_2 = batch_dataframes['dgro_batch_2']

# The third batch
dgro_batch_3 = batch_dataframes['dgro_batch_3']

# The fourth batch
dgro_batch_4 = batch_dataframes['dgro_batch_4']

# The fifth batch
dgro_batch_5 = batch_dataframes['dgro_batch_5']


