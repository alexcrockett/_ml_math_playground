import sys
import os

# Add the path to the 'data' directory (one level up from 'old_batching_files')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the path to the 'imports' directory (two levels up and then into 'imports'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))

# Import the module
from sud.sud.imports import sud_import_daily as sud

# Call the main function to get the data frames
all_frames = sud.main()

# Function to create old_batching_files of 100 for each stock
def create_batches(data_frames, batch_size=100):
	batched_data = {}
	for stock, df in data_frames.items():
		batches = [df.iloc[i:i + batch_size] for i in range(0, len(df), batch_size)]
		batched_data[stock] = batches
	return batched_data

# Create old_batching_files
batched_data = create_batches(all_frames)
