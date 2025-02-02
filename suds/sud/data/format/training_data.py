# Import libraries
import sys
import os
import numpy as np
from scipy.stats import norm
import math

# Import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))
from suds.sud.imports._import_ import main as bat

# Fetch and format data
all_batches = bat()

def import_fu():
	return [fu for fu in all_batches.values()]

def batch_values(value_dat):
	# Build the Differences set
	start = value_dat  # Start value
	stop = np.roll(value_dat, -1, axis=0)  # Stop value (shifted by -1)
	change = stop - start  # Calculate the change
	change = np.transpose(change)  # Transpose array
	change[np.isnan(change)] = np.nanmean(change)  # Remove NaN

	change_mag = np.linalg.norm(change, axis=0)  # Magnitude
	change_mag[change_mag == 0] = 1  # Remove zeroes
	scaled = change / change_mag  # Scale by magnitude
	manhattan = np.linalg.norm(scaled, ord=1, axis=0)  # Normalize
	manhattan[manhattan == 0] = 1  # Remove zeroes
	transformed_data = scaled / manhattan  # Scale down to range

	exclude_volume = change[:-1, :]  # Remove volume for statistics
	values_var = np.var(exclude_volume, axis=0)  # Variance
	values_std = np.std(exclude_volume, axis=0)  # Standard Deviation

	# Build the probability portion of the matrix
	value_signs = np.sign(change)
	mean_values = np.mean(change, axis=0)
	std_values = np.std(change, axis=0)
	std_values[std_values == 0] = math.pi * 0.0000001
	numerator = change - mean_values
	numerator[numerator == 0] = math.pi * 0.0000001
	z_data = numerator / std_values
	p_values = norm.cdf(z_data)
	signed_p = p_values * value_signs

	# Prepend original values
	# origin_t = np.transpose(start)
	value_stack = np.vstack([values_var, values_std, transformed_data, signed_p])  # Add stats as features
	values = value_stack
	return values

def generate_batches(value_dat, num_batches=5):
	return [batch_values(value_dat[i]) for i in range(num_batches)]

def batch_all_values(value_dat):
	num_batches = 5  # Define number of old_batching_files
	return generate_batches(value_dat, num_batches)

def main():
	formatted_data = import_fu()
	return [batch_all_values(data) for data in formatted_data]

# Main execution block for formatting data
if __name__ == "__main__":
	all_batches_formatted = main()
	print(all_batches_formatted)  # Optional: Print to verify the output
