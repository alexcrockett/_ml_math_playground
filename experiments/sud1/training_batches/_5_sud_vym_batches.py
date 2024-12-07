import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


vym = 'VYM'
batch_vym = batched_data[vym]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_vym):
	print(f"\nBatch {i+1} for {vym}:\n")
	vym_batches = pd.DataFrame(batch)
	batch_dataframes[f'vym_batch_{i+1}'] = vym_batches  # Store in dictionary

# The first batch
vym_batch_1 = batch_dataframes['vym_batch_1']

# The second batch
vym_batch_2 = batch_dataframes['vym_batch_2']

# The third batch
vym_batch_3 = batch_dataframes['vym_batch_3']

# The fourth batch
vym_batch_4 = batch_dataframes['vym_batch_4']

# The fifth batch
vym_batch_5 = batch_dataframes['vym_batch_5']


