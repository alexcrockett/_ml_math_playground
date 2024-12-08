import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


hdef = 'HDEF'
batch_hdef = batched_data[hdef]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_hdef):
	print(f"\nBatch {i+1} for {hdef}:\n")
	hdef_batches = pd.DataFrame(batch)
	batch_dataframes[f'hdef_batch_{i+1}'] = hdef_batches  # Store in dictionary

# The first batch
hdef_batch_1 = batch_dataframes['hdef_batch_1']

# The second batch
hdef_batch_2 = batch_dataframes['hdef_batch_2']

# The third batch
hdef_batch_3 = batch_dataframes['hdef_batch_3']

# The fourth batch
hdef_batch_4 = batch_dataframes['hdef_batch_4']

# The fifth batch
hdef_batch_5 = batch_dataframes['hdef_batch_5']


