# Import libraries
import h5py

# Create h5 file to store weights in
def save_weights_to_hdf5(model, file_name='weights.h5'):
	with h5py.File(file_name, 'w') as hf:
		for i, layer in enumerate(model.layers):
			hf.create_dataset(f'layer_{i}_weights', data=layer.get_weights()[0])
			hf.create_dataset(f'layer_{i}_biases', data=layer.get_weights()[1])

def load_weights_from_hdf5(model, file_name='weights.h5'):
	with h5py.File(file_name, 'r') as hf:
		for i, layer in enumerate(model.layers):
			weights = hf[f'layer_{i}_weights'][:]
			biases = hf[f'layer_{i}_biases'][:]
			model.layers[i].set_weights([weights, biases])
