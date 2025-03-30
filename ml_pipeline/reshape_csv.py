import pandas as pd
import numpy as np

# Parameters
import os
log_files = sorted([f for f in os.listdir() if f.startswith("log_") and f.endswith(".csv")])
input_file = log_files[-1] if log_files else None
if input_file is None:
    raise FileNotFoundError("No log_*.csv file found in this directory.")
print(f"Using latest file: {input_file}")

seq_len = 20  # number of timesteps

# Load CSV
df = pd.read_csv(input_file)
features = ["rms", "fft_peak", "fft_centroid"]  # adjust as needed
X_raw = df[features].values
y_raw = df["label"].values

X_seq = []
y_seq = []

# Reshape to sequences
for i in range(len(X_raw) - seq_len):
    X_seq.append(X_raw[i:i+seq_len])
    y_seq.append(y_raw[i+seq_len])  # label is the class after the sequence

X_seq = np.array(X_seq)
y_seq = np.array(y_seq)

# Save numpy arrays
np.save("X_sequences.npy", X_seq)
np.save("y_sequences.npy", y_seq)

print("Saved: X_sequences.npy and y_sequences.npy")
