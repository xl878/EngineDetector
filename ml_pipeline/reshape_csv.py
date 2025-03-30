import pandas as pd
import numpy as np

# Parameters
input_file = "data.csv"
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
