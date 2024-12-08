import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


xlf = 'XLF'
batch_xlf = batched_data[xlf]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_xlf):
	print(f"\nBatch {i+1} for {xlf}:\n")
	xlf_batches = pd.DataFrame(batch)
	batch_dataframes[f'xlf_batch_{i+1}'] = xlf_batches  # Store in dictionary

# The first batch
xlf_batch_1 = batch_dataframes['xlf_batch_1']

# The second batch
xlf_batch_2 = batch_dataframes['xlf_batch_2']

# The third batch
xlf_batch_3 = batch_dataframes['xlf_batch_3']

# The fourth batch
xlf_batch_4 = batch_dataframes['xlf_batch_4']

# The fifth batch
xlf_batch_5 = batch_dataframes['xlf_batch_5']


