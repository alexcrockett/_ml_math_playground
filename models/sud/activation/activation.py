# Import libraries
import sys
import os
import h5py
import numpy as np
import keras
from keras import Sequential

# Import relevant files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.sud.data.formatted_data import labels as ldat

# Import data
def t_data(index, batch):
	training_values = ldat.get_specific_batch(index, batch)

# Convert to tensors
# Build model
for epoch in range(num_epochs):
	# Training code here...
	save_weights_to_hdf5(model, file_name=f'weights_epoch_{epoch}.h5')