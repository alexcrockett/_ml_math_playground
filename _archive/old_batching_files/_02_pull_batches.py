import os
import sys

# Import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import the necessary modules
import _01_sud_batches as bat

data = bat.main()

def get_training_data():
	training_data = {}
	for d in data:
		training_data.update(d)
	return training_data

def main():
	training_data = get_training_data()
	print(training_data)
	return training_data

if __name__ == "__main__":
	main()
