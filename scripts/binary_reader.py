import numpy as np

# Create a fake acoustic signal for testing
signal = np.random.randint(-1000, 1000, size=2048, dtype=np.int16)

# Save the signal to a binary file
signal.tofile("data/raw/test_signal.bin")

# Read the binary file
loaded_signal = np.fromfile("data/raw/test_signal.bin", dtype=np.int16)

print(f"Number of samples: {len(loaded_signal)}")
print(f"First 10 samples:")
print(loaded_signal[:10])