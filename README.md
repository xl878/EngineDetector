# ML Pipeline Overview

This folder contains training scripts and data preparation tools for supervised learning models on vibration sensor data.

## Folder Contents:

- `train_rf.py`: Random Forest classifier training on window-averaged features (RMS, FFT peak, etc.)
- `train_lstm.py`: LSTM sequence model for detecting patterns over time
- `reshape_csv.py`: Utility script to convert flat CSV data into time-sequenced numpy arrays
- `log_serial_to_csv.py`: Live logger to save Arduino vibration data to `.csv`
- `run_pipeline.sh`: End-to-end pipeline runner for data reshaping, training, evaluation, and saving
- `model_summary_*.txt`: Saved output summaries for model evaluation and comparison

## Suggested Workflow:

1. Export your windowed CSV from the web app
2. Use `log_serial_to_csv.py` to collect real-time sensor data (optional)
3. Run `reshape_csv.py` to prepare sequence inputs (X, y arrays)
4. Train and evaluate models with:
   - `train_rf.py` for fast tree-based classification
   - `train_lstm.py` for temporal deep learning
5. Summarize results into `.txt` for review

All scripts can be extended for model saving, evaluation, and visualization.

---

## Model Evaluation Summary (2025-03-30)

| Model           | Accuracy | Training Time | Model Size |
|----------------|----------|----------------|-------------|
| Random Forest  | 88.00%   | 3.2s           | 234 KB      |
| LSTM           | 91.00%   | 15.4s          | 1.2 MB      |

_Notes_:  
- Random Forest: fast and compact  
- LSTM: higher accuracy for time-sequence patterns

---

## Requirements

Install the necessary Python packages:

```bash
pip install numpy pandas scikit-learn tensorflow
```

---

## GitHub Usage Tips

- Use `run_pipeline.sh` to execute all steps in one command
- Push `.txt` and model files for reproducibility:

```bash
git add model_summary_*.txt *.pkl *.h5
```

- Sync with GitHub before pushing if needed:

```bash
git pull origin main
```

---

For questions or collaboration, contact the maintainer or open an issue in the repo.

