import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


djia = 'DJIA'
batch_djia = batched_data[djia]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_djia):
	print(f"\nBatch {i+1} for {djia}:\n")
	djia_batches = pd.DataFrame(batch)
	batch_dataframes[f'djia_batch_{i+1}'] = djia_batches  # Store in dictionary

# The first batch
djia_batch_1 = batch_dataframes['djia_batch_1']

# The second batch
djia_batch_2 = batch_dataframes['djia_batch_2']

# The third batch
djia_batch_3 = batch_dataframes['djia_batch_3']

# The fourth batch
djia_batch_4 = batch_dataframes['djia_batch_4']

# The fifth batch
djia_batch_5 = batch_dataframes['djia_batch_5']


