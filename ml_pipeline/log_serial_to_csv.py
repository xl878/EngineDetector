import serial
import csv
from datetime import datetime

# Settings
port = '/dev/cu.usbmodem2101' 
baud = 115200
outfile = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Open Serial and CSV
ser = serial.Serial(port, baud, timeout=1)
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['timestamp', 'accZ', 'mov_avg', 'rms', 'fft_peak', 'label']
    writer.writerow(header)
    print(f"[LOGGING] Writing to {outfile}... Press Ctrl+C to stop.")

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line and line.count(',') == 5:
                print(line)
                writer.writerow(line.split(','))
    except KeyboardInterrupt:
        print("\n[LOGGING STOPPED]")
        ser.close()
