#!/bin/bash

echo "🔍 Looking for the latest log file..."
cd "$(dirname "$0")"  # go to script directory
latest_csv=$(ls -t log_*.csv 2>/dev/null | head -n 1)

if [ -z "$latest_csv" ]; then
  echo "❌ No log_*.csv file found. Please run log_serial_to_csv.py first."
  exit 1
fi

echo "📄 Found: $latest_csv"
echo "📦 Reshaping CSV into sequences..."
python3 reshape_csv.py

echo "🌲 Training Random Forest..."
python3 train_rf.py

echo "🧠 Training LSTM..."
python3 train_lstm.py

echo "✅ Pipeline complete! Models saved as rf_model.pkl and lstm_model.h5"
