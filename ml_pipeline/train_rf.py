import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load CSV
import os
log_files = sorted([f for f in os.listdir() if f.startswith("log_") and f.endswith(".csv")])
input_file = log_files[-1] if log_files else None
if input_file is None:
    raise FileNotFoundError("No log_*.csv file found.")
print(f"Using latest file: {input_file}")
df = pd.read_csv('log_20250330_115813.csv')

# Features and labels
expected_features = ["accZ", "mov_avg", "rms", "fft_peak"]
missing = [f for f in expected_features if f not in df.columns]

if missing:
    print(f"⚠️ Warning: Missing expected features: {missing}")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    excluded = ["timestamp", "label"]
    features = [col for col in numeric_cols if col not in excluded]
    print(f"→ Using auto-detected features: {features}")
else:
    features = expected_features

X = df[features]
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("Training Random Forest...")
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Validation Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score, classification_report

# After predicting
accuracy = accuracy_score(y_test, y_pred)

# Save accuracy to result file
with open("rf_result.txt", "w") as f:
    f.write(f"{accuracy:.4f}")

# Save the input file used
with open("used_log.txt", "w") as f:
    f.write(input_file)

# Save model
joblib.dump(clf, "rf_model.pkl")
print("Model saved to rf_model.pkl")
