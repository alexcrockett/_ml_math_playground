import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


vymi = 'VYMI'
batch_vymi = batched_data[vymi]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_vymi):
	print(f"\nBatch {i+1} for {vymi}:\n")
	vymi_batches = pd.DataFrame(batch)
	batch_dataframes[f'vymi_batch_{i+1}'] = vymi_batches  # Store in dictionary

# The first batch
vymi_batch_1 = batch_dataframes['vymi_batch_1']

# The second batch
vymi_batch_2 = batch_dataframes['vymi_batch_2']

# The third batch
vymi_batch_3 = batch_dataframes['vymi_batch_3']

# The fourth batch
vymi_batch_4 = batch_dataframes['vymi_batch_4']

# The fifth batch
vymi_batch_5 = batch_dataframes['vymi_batch_5']


