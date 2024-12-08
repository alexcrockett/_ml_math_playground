import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


hyg = 'HYG'
batch_hyg = batched_data[hyg]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_hyg):
	print(f"\nBatch {i+1} for {hyg}:\n")
	hyg_batches = pd.DataFrame(batch)
	batch_dataframes[f'hyg_batch_{i+1}'] = hyg_batches  # Store in dictionary

# The first batch
hyg_batch_1 = batch_dataframes['hyg_batch_1']

# The second batch
hyg_batch_2 = batch_dataframes['hyg_batch_2']

# The third batch
hyg_batch_3 = batch_dataframes['hyg_batch_3']

# The fourth batch
hyg_batch_4 = batch_dataframes['hyg_batch_4']

# The fifth batch
hyg_batch_5 = batch_dataframes['hyg_batch_5']


