import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


lit = 'LIT'
batch_lit = batched_data[lit]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_lit):
	print(f"\nBatch {i+1} for {lit}:\n")
	lit_batches = pd.DataFrame(batch)
	batch_dataframes[f'lit_batch_{i+1}'] = lit_batches  # Store in dictionary

# The first batch
lit_batch_1 = batch_dataframes['lit_batch_1']

# The second batch
lit_batch_2 = batch_dataframes['lit_batch_2']

# The third batch
lit_batch_3 = batch_dataframes['lit_batch_3']

# The fourth batch
lit_batch_4 = batch_dataframes['lit_batch_4']

# The fifth batch
lit_batch_5 = batch_dataframes['lit_batch_5']


