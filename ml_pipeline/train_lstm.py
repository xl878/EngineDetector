import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Load data
X = np.load("X_sequences.npy")  # shape: (samples, timesteps, features)
y = np.load("y_sequences.npy")

# Encode labels
num_classes = len(np.unique(y))
y = to_categorical(y, num_classes=num_classes)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
model = Sequential()
model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train
print("Training LSTM...")
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"Validation Accuracy: {acc:.4f}")
# Save LSTM accuracy to file for summary
with open("lstm_result.txt", "w") as f:
    f.write(f"{acc:.4f}")

# Save model
model.save("lstm_model.h5")
print("Model saved to lstm_model.h5")
