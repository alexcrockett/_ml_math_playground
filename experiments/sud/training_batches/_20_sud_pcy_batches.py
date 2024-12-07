import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


pcy = 'PCY'
batch_pcy = batched_data[pcy]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_pcy):
	print(f"\nBatch {i+1} for {pcy}:\n")
	pcy_batches = pd.DataFrame(batch)
	batch_dataframes[f'pcy_batch_{i+1}'] = pcy_batches  # Store in dictionary

# The first batch
pcy_batch_1 = batch_dataframes['pcy_batch_1']

# The second batch
pcy_batch_2 = batch_dataframes['pcy_batch_2']

# The third batch
pcy_batch_3 = batch_dataframes['pcy_batch_3']

# The fourth batch
pcy_batch_4 = batch_dataframes['pcy_batch_4']

# The fifth batch
pcy_batch_5 = batch_dataframes['pcy_batch_5']


