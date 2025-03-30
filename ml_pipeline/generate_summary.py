from datetime import datetime

# Read saved results
with open("rf_result.txt") as f:
    rf_accuracy = float(f.read())

with open("lstm_result.txt") as f:
    lstm_accuracy = float(f.read())

# Timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
summary_filename = f"model_summary_{timestamp}.txt"

# Format summary content
summary = f"""Model Training Summary – {timestamp}

Random Forest:
– Validation Accuracy: {rf_accuracy:.4f}

LSTM:
– Validation Accuracy: {lstm_accuracy:.4f}
"""

# Save to file
with open(summary_filename, "w") as f:
    f.write(summary)

print(f"[✓] Summary saved to: {summary_filename}")
