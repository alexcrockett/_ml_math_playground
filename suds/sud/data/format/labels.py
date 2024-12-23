# Import libraries
import sys
import os
import numpy as np

# Import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import files
from suds.sud.data.format.training_data import import_fu, batch_all_values

# Retrieve formatted data
formatted_data = import_fu()

all_batches = []
for data in formatted_data:
	batches = batch_all_values(data)
	all_batches.append(batches)

# Function to get a specific batch for a specific stock
def get_specific_batch(stock_index, batch_number):
	try:
		return all_batches[stock_index][batch_number]
	except IndexError:
		print("Invalid stock index or batch number")
		return None

# Build our labels
def label_calc(stock_index, batch_number):
	label_holder = []

	# Get specific batch
	data_for_labels = get_specific_batch(stock_index, batch_number)

	for index, batch in enumerate(data_for_labels):
		slice_for_labels = batch[5:9]  # Slice the relevant part of the data
		quantiles = [np.quantile(slice_for_labels, q) for q in np.arange(0.1, 1, 0.1)]  # Calculate quantiles
		direction = np.sign(slice_for_labels[1])  # Get the sign direction (assuming you need this for labels)
		sums = np.sum(slice_for_labels, axis=0)  # Sum the slice

		# Binning based on quantiles
		for s in sums:
			for i, quant in enumerate(quantiles):
				if s <= quant:
					label_holder.append((i+1)/10)  # Assign 0.1, 0.2, ..., 0.9 based on quantile
					break
			else:
				label_holder.append(0.9)  # Default to 0.9 if it exceeds the last quantile

	labels = np.array(label_holder) * direction  # Convert to array and multiply by direction
	return labels

