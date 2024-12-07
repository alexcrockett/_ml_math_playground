import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


jnk = 'JNK'
batch_jnk = batched_data[jnk]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_jnk):
	print(f"\nBatch {i+1} for {jnk}:\n")
	jnk_batches = pd.DataFrame(batch)
	batch_dataframes[f'jnk_batch_{i+1}'] = jnk_batches  # Store in dictionary

# The first batch
jnk_batch_1 = batch_dataframes['jnk_batch_1']

# The second batch
jnk_batch_2 = batch_dataframes['jnk_batch_2']

# The third batch
jnk_batch_3 = batch_dataframes['jnk_batch_3']

# The fourth batch
jnk_batch_4 = batch_dataframes['jnk_batch_4']

# The fifth batch
jnk_batch_5 = batch_dataframes['jnk_batch_5']


