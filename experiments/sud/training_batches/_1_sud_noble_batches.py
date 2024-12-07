import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


nobl = 'NOBL'
batch_nobl = batched_data[nobl]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_nobl):
	print(f"\nBatch {i+1} for {nobl}:\n")
	nobl_batches = pd.DataFrame(batch)
	batch_dataframes[f'nobl_batch_{i+1}'] = nobl_batches  # Store in dictionary

# The first batch
nob_batch_1 = batch_dataframes['nobl_batch_1']

# The second batch
nob_batch_2 = batch_dataframes['nobl_batch_2']

# The third batch
nob_batch_3 = batch_dataframes['nobl_batch_3']

# The fourth batch
nob_batch_4 = batch_dataframes['nobl_batch_4']

# The fifth batch
nob_batch_5 = batch_dataframes['nobl_batch_5']


