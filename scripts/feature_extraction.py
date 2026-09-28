import numpy as np

# Load Signal
signal = np.fromfile("data/raw/test_signal.bin", dtype=np.int16)

# Convert to float for calculations
signal = signal.astype(float)

# RMS
rms = np.sqrt(np.mean(signal**2))

# Peak Amplitude
peak_amplitude = np.max(np.abs(signal))

#Signal Energy
energy = np.sum(signal**2)

# Print Features
print("Extracted Features:")
print("--------------------")
print(f"RMS: {rms:.2f}")
print(f"Peak Amplitude: {peak_amplitude:.2f}")
print(f"Signal Energy: {energy:.2f}")