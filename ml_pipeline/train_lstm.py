import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load CSV
df = pd.read_csv("log_20250330_115813.csv")

# Load features and label
X = df[["accZ", "mov_avg", "rms", "fft_peak"]].values
y_raw = df["label"].values

# Encode string labels to integers
le = LabelEncoder()
y_encoded = le.fit_transform(y_raw)
y = to_categorical(y_encoded)

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape input for LSTM: (samples, timesteps, features)
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Build model
model = Sequential()
model.add(LSTM(32, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"Validation Accuracy: {acc:.4f}")

# Save LSTM accuracy to file for summary
with open("lstm_result.txt", "w") as f:
    f.write(f"{acc:.4f}")

# Save model
model.save("lstm_model.h5")
