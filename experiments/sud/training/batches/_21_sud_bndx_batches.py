import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


bndx = 'BNDX'
batch_bndx = batched_data[bndx]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_bndx):
	print(f"\nBatch {i+1} for {bndx}:\n")
	bndx_batches = pd.DataFrame(batch)
	batch_dataframes[f'bndx_batch_{i+1}'] = bndx_batches  # Store in dictionary

# The first batch
bndx_batch_1 = batch_dataframes['bndx_batch_1']

# The second batch
bndx_batch_2 = batch_dataframes['bndx_batch_2']

# The third batch
bndx_batch_3 = batch_dataframes['bndx_batch_3']

# The fourth batch
bndx_batch_4 = batch_dataframes['bndx_batch_4']

# The fifth batch
bndx_batch_5 = batch_dataframes['bndx_batch_5']


