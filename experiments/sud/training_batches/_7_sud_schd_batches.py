import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _0_process_data

batched_data = _0_process_data.batched_data


schd = 'SCHD'
batch_schd = batched_data[schd]

# Dictionary to store each batch DataFrame
batch_dataframes = {}

for i, batch in enumerate(batch_schd):
	print(f"\nBatch {i+1} for {schd}:\n")
	schd_batches = pd.DataFrame(batch)
	batch_dataframes[f'schd_batch_{i+1}'] = schd_batches  # Store in dictionary

# The first batch
schd_batch_1 = batch_dataframes['schd_batch_1']

# The second batch
schd_batch_2 = batch_dataframes['schd_batch_2']

# The third batch
schd_batch_3 = batch_dataframes['schd_batch_3']

# The fourth batch
schd_batch_4 = batch_dataframes['schd_batch_4']

# The fifth batch
schd_batch_5 = batch_dataframes['schd_batch_5']


