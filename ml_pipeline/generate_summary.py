import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import os

# Automatically select latest log file
log_files = sorted([f for f in os.listdir() if f.startswith("log_") and f.endswith(".csv")])
if not log_files:
    raise FileNotFoundError("No log_*.csv file found")
input_file = log_files[-1]
print(f"Using log file: {input_file}")

# Load data
seq_len = 20  # number of timesteps
raw_df = pd.read_csv(input_file)
features = ["accZ", "mov_avg", "rms", "fft_peak"]
X_data = raw_df[features].values
y_data = raw_df["label"].astype("category").cat.codes.values

# Create sequences
def create_sequences(X, y, seq_len):
    Xs, ys = [], []
    for i in range(len(X) - seq_len):
        Xs.append(X[i:i + seq_len])
        ys.append(y[i + seq_len])
    return np.array(Xs), np.array(ys)

X, y = create_sequences(X_data, y_data, seq_len)
y = to_categorical(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build LSTM model
model = Sequential()
model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"Validation Accuracy: {acc:.4f}")

# Save LSTM accuracy to file for summary
with open("lstm_result.txt", "w") as f:
    f.write(f"{acc:.4f}")

# Save the input file used
with open("used_log.txt") as f:
    log_used = f.read().strip()

summary += f"\nInput data used: {log_used}\n"

# Save model
model.save("lstm_model.h5")
