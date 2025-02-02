# Import libraries
import sys
import os
import h5py
import numpy as np
import keras
import tensorflow as tf

# Import relevant files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from suds.sud.data.format import labels as ldat
from weights import save_weights_to_hdf5, load_weights_from_hdf5

# Process the data

# Custom callback to log loss after each batch
class LossHistory(tf.keras.callbacks.Callback):
	def on_batch_end(self, batch, logs=None):
		print(f'Batch {batch + 1}: Loss = {logs["loss"]:.4f}')

# Primary training function
def batch_training_data(ldat, model, initial_weights_file=None):
	num_stocks = 39
	num_batches_per_stock = 5
	num_inputs_per_batch = 100

	# Load initial weights
	if initial_weights_file:
		try:
			load_weights_from_hdf5(model, initial_weights_file)
			print(f"Loaded weights from {initial_weights_file}")
		except FileNotFoundError:
			print(f"File {initial_weights_file} not found. Starting with random weights.")

	for batch_num in range(num_batches_per_stock):
		for stock_index in range(num_stocks):
			# Get the specific batch of stock data
			stock_x = ldat.get_specific_batch(stock_index, batch_num)

			# Calculate the labels for the batch
			labels_y = ldat.label_calc(stock_index, batch_num)

			# Iterate through the 100 inputs for each batch
			for input_index in range(num_inputs_per_batch):
				# Extract the features for the current input
				features = stock_x[:, input_index]
				features = tf.convert_to_tensor(features, dtype=tf.float32)

				# Extract the corresponding label
				label = labels_y[:, input_index]
				label = tf.convert_to_tensor(label, dtype=tf.float32)

				# Ensure labels match expected shape
				label = tf.expand_dims(label, axis=0)

				# Run the features through the model
				model.train_on_batch(tf.expand_dims(features, axis=0), label)

				# Optional: print for debugging
				print(f'Batch {batch_num + 1}, Stock {stock_index + 1}, Input {input_index + 1}:')
				print('Features:', features.numpy())
				print('Label:', label.numpy())

		# Save the model weights after each batch
		save_weights_to_hdf5(model, file_name=f'weights_batch_{batch_num + 1}.h5')

	# Optionally, save the model weights after all old_batching_files
	save_weights_to_hdf5(model, file_name='final_weights.h5')

# Define the Keras model with GELU activation and tanh output layer
input_dim = 7  # Number of features per input (7 rows in your data)
model = tf.keras.Sequential([
	tf.keras.layers.Input(shape=(input_dim,)),
	tf.keras.layers.Dense(64, activation='gelu'),
	tf.keras.layers.Dense(64, activation='gelu'),
	tf.keras.layers.Dense(1, activation='tanh')  # Use tanh for the output layer
])

# Compile the model with mean squared error loss function for regression-like output
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Specify the initial weights file if you have pre-trained weights
initial_weights_file = 'initial_weights.h5'  # Adjust this as needed
batch_training_data(ldat, model, initial_weights_file=initial_weights_file)
