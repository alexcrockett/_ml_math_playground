import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


kre = 'KRE'
batch_kre = batched_data[kre]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_kre):
	print(f"\nBatch {i+1} for {kre}:\n")
	kre_batches = pd.DataFrame(batch)
	batch_dataframes[f'kre_batch_{i+1}'] = kre_batches  # Store in dictionary

# The first batch
kre_batch_1 = batch_dataframes['kre_batch_1']

# The second batch
kre_batch_2 = batch_dataframes['kre_batch_2']

# The third batch
kre_batch_3 = batch_dataframes['kre_batch_3']

# The fourth batch
kre_batch_4 = batch_dataframes['kre_batch_4']

# The fifth batch
kre_batch_5 = batch_dataframes['kre_batch_5']


