import numpy as np
import sys
import os

from sud.sud.data.format.labels import get_specific_batch, label_calc

# Import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'format')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'imports')))
# Import files
from sud.sud.imports import sud_import_daily
from sud.sud.data.format import labels as ldat

stocks = sud_import_daily.training_stocks
initial_weights = np.random.rand(7,)

def innit_h5_file(file_name='weights.h5'):
	with h5py.File(file_name, 'w') as f:
		w1 = f.create_dataset(name='weights_1', shape=(7,), dtype='float')
