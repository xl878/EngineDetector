def flag_anomalies(rms, peak, centroid):
    if rms > 1.2 or peak > 2.0:
        return "Anomaly"
    return "Normal"
