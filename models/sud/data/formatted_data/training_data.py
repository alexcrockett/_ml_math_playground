# Import libraries
import sys
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'batches')))

# Import files
from models.sud.data.batches.__training_data import training_data

# Import functions
from models.sud.data.batches.__training_data import (nobl_fu, vymi_fu, pey_fu, xle_fu, vym_fu,
													 hdv_fu, glncy_fu, dgro_fu, vb_fu, jnk_fu,
													 hyg_fu, schd_fu, ixus_fu, djia_fu, lit_fu,
													 sphd_fu, iscf_fu, hscz_fu, hdef_fu, pcy_fu,
													 bndx_fu, smx_fu, hefa_fu, iyk_fu, usoi_fu,
													 xlf_fu, vfh_fu, kre_fu, iyf_fu, fncl_fu,
													 qqq_fu, spy_fu, vti_fu, itot_fu, xlk_fu,
													 xly_fu, xlv_fu, eem_fu, veu_fu)

# List of the data functions
dat = [nobl_fu(training_data), vymi_fu(training_data), pey_fu(training_data),
	   xle_fu(training_data), vym_fu(training_data), hdv_fu(training_data),
	   glncy_fu(training_data), dgro_fu(training_data), vb_fu(training_data),
	   jnk_fu(training_data), hyg_fu(training_data), schd_fu(training_data),
	   ixus_fu(training_data), djia_fu(training_data), lit_fu(training_data),
	   sphd_fu(training_data), iscf_fu(training_data), hscz_fu(training_data),
	   hdef_fu(training_data), pcy_fu(training_data), bndx_fu(training_data),
	   smx_fu(training_data), hefa_fu(training_data), iyk_fu(training_data),
	   usoi_fu(training_data), xlf_fu(training_data), xly_fu(training_data),
	   vfh_fu(training_data), kre_fu(training_data), iyf_fu(training_data),
	   fncl_fu(training_data), qqq_fu(training_data), spy_fu(training_data),
	   vti_fu(training_data), itot_fu(training_data), xlk_fu(training_data),
	   xlv_fu(training_data), eem_fu(training_data), veu_fu(training_data)]

# Format for use
def import_fu():
	values = []
	for fu in dat:
		values.append(fu)
	return values

# Build the arrays
def batch_values(value_dat):
	stop = pd.DataFrame(value_dat)  # End value of difference
	start = pd.DataFrame(value_dat).shift(periods=1)  # Start value of difference
	stop_array = stop.to_numpy()  # Convert to array
	start_array = start.to_numpy()  # Convert to array
	start_array[np.isnan(start_array)] = np.mean(start_array[np.logical_not(np.isnan(start_array))])  # Remove NaN
	change = stop_array - start_array  # Calc. difference
	change = np.transpose(change)  # Transpose array so we have columns per stock

	change_mag = np.linalg.norm(change, axis=0)  # Magnitude
	change_mag[change_mag == 0] = 1  # Remove zeroes
	scaled = change * change_mag  # Scale by magnitude
	manhatten = np.linalg.norm(scaled, ord=1, axis=0)  # Normalize
	manhatten[manhatten == 0] = 1  # Remove eroes
	values = scaled / manhatten  # Scale down to range

	exclude_volume = change[:-1, :]  # Remove volume for statistics
	values_var = np.var(exclude_volume, axis=0)  # Variance
	values_std = np.std(exclude_volume, axis=0)  # Standard Deviation
	values = np.vstack([values, values_var, values_std])  # Add stats to array as features

	return values  # Return the data

# Now we create functions to call batches

# Generate the batches and create a list
def generate_batches(value_dat, num_batches=5):
	batches = []
	for i in range(num_batches):
		batch = batch_values(value_dat[i])
		batches.append(batch)
	return batches

def batch_all_values(value_dat):
	num_batches = 5  # Define how many batches you want to create
	return generate_batches(value_dat, num_batches)

# Usage in another file
if __name__ == "__main__":
	formatted_data = import_fu()
	all_batches = []
	for data in formatted_data:
		batches = batch_all_values(data)
		all_batches.append(batches)
