from tqdm import tqdm
import time

for i in tqdm(range(100)):
	time.sleep(0.1)  # Simulate a time-consuming task

# Version 2
import multiprocessing
from tqdm import tqdm

def process_data(data):
	# Simulate some work
	for i in tqdm(range(len(data)), desc=f"Process {multiprocessing.current_process().name}"):
		# Perform your processing here
		pass

if __name__ == '__main__':
	data = [range(100), range(200), range(150)]  # Example data
	with multiprocessing.Pool() as pool:
		pool.map(process_data, data)