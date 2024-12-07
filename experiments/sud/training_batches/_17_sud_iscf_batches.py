import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


iscf = 'ISCF'
batch_iscf = batched_data[iscf]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_iscf):
	print(f"\nBatch {i+1} for {iscf}:\n")
	iscf_batches = pd.DataFrame(batch)
	batch_dataframes[f'iscf_batch_{i+1}'] = iscf_batches  # Store in dictionary

# The first batch
iscf_batch_1 = batch_dataframes['iscf_batch_1']

# The second batch
iscf_batch_2 = batch_dataframes['iscf_batch_2']

# The third batch
iscf_batch_3 = batch_dataframes['iscf_batch_3']

# The fourth batch
iscf_batch_4 = batch_dataframes['iscf_batch_4']

# The fifth batch
iscf_batch_5 = batch_dataframes['iscf_batch_5']


