import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


iyk = 'IYK'
batch_iyk = batched_data[iyk]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_iyk):
	print(f"\nBatch {i+1} for {iyk}:\n")
	iyk_batches = pd.DataFrame(batch)
	batch_dataframes[f'iyk_batch_{i+1}'] = iyk_batches  # Store in dictionary

# The first batch
iyk_batch_1 = batch_dataframes['iyk_batch_1']

# The second batch
iyk_batch_2 = batch_dataframes['iyk_batch_2']

# The third batch
iyk_batch_3 = batch_dataframes['iyk_batch_3']

# The fourth batch
iyk_batch_4 = batch_dataframes['iyk_batch_4']

# The fifth batch
iyk_batch_5 = batch_dataframes['iyk_batch_5']


