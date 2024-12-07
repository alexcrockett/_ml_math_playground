import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


hscz = 'HSCZ'
batch_hscz = batched_data[hscz]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_hscz):
	print(f"\nBatch {i+1} for {hscz}:\n")
	hscz_batches = pd.DataFrame(batch)
	batch_dataframes[f'hscz_batch_{i+1}'] = hscz_batches  # Store in dictionary

# The first batch
hscz_batch_1 = batch_dataframes['hscz_batch_1']

# The second batch
hscz_batch_2 = batch_dataframes['hscz_batch_2']

# The third batch
hscz_batch_3 = batch_dataframes['hscz_batch_3']

# The fourth batch
hscz_batch_4 = batch_dataframes['hscz_batch_4']

# The fifth batch
hscz_batch_5 = batch_dataframes['hscz_batch_5']


