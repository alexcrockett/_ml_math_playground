import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


pey = 'PEY'
batch_pey = batched_data[pey]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_pey):
	print(f"\nBatch {i+1} for {pey}:\n")
	pey_batches = pd.DataFrame(batch)
	batch_dataframes[f'pey_batch_{i+1}'] = pey_batches  # Store in dictionary

# The first batch
pey_batch_1 = batch_dataframes['pey_batch_1']

# The second batch
pey_batch_2 = batch_dataframes['pey_batch_2']

# The third batch
pey_batch_3 = batch_dataframes['pey_batch_3']

# The fourth batch
pey_batch_4 = batch_dataframes['pey_batch_4']

# The fifth batch
pey_batch_5 = batch_dataframes['pey_batch_5']


