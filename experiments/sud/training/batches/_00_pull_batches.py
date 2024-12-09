# This file will create a set of arrays for each batch belonging to each stock

import pandas as pd
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the necessary module from the parent directory
import _01_sud_noble_batches as train1

# Function to retrieve the list of DataFrames
def get_nob_list():
	nob_list = train1.main()
	return nob_list

# Function to pull the DataFrames
def pull_dataframes(nob_list):
	if len(nob_list) < 5:
		raise ValueError("The list does not contain enough items")

	nob1, nob2, nob3, nob4, nob5 = nob_list[0], nob_list[1], nob_list[2], nob_list[3], nob_list[4]
	return nob1, nob2, nob3, nob4, nob5

# Example usage
if __name__ == "__main__":
	nob_list = get_nob_list()
	nob1, nob2, nob3, nob4, nob5 = pull_dataframes(nob_list)
	print(nob1.head())




