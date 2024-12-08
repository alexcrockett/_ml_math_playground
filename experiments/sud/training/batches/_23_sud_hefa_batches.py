import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


hefa = 'HEFA'
batch_hefa = batched_data[hefa]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_hefa):
	print(f"\nBatch {i+1} for {hefa}:\n")
	hefa_batches = pd.DataFrame(batch)
	batch_dataframes[f'hefa_batch_{i+1}'] = hefa_batches  # Store in dictionary

# The first batch
hefa_batch_1 = batch_dataframes['hefa_batch_1']

# The second batch
hefa_batch_2 = batch_dataframes['hefa_batch_2']

# The third batch
hefa_batch_3 = batch_dataframes['hefa_batch_3']

# The fourth batch
hefa_batch_4 = batch_dataframes['hefa_batch_4']

# The fifth batch
hefa_batch_5 = batch_dataframes['hefa_batch_5']


