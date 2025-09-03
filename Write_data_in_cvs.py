# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 14:28:16 2025

@author: beckylin
"""

import serial
from datetime import datetime
import csv
import os

# Settings
PORT = 'COM16'
BAUDRATE = 115200
DATA_DIR = './vibration_data'

def create_csv():
    now = datetime.now()
    folder = os.path.join(DATA_DIR, now.strftime('%Y%m%d'))
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, now.strftime('%Y%m%d%H%M') + '.csv')
    file = open(filename, 'a', newline='')
    writer = csv.writer(file)
    writer.writerow(['DATETIME', 'X', 'Y', 'Z'])
    return file, writer, now

def main():
    ser = serial.Serial(PORT, BAUDRATE)
    file, writer, file_time = create_csv()

    print("Reading data... Press Ctrl+C to stop.")

    try:
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line and len(line) >= 20:
                timestamp = datetime.now().strftime('%H%M%S%f')[:9]
                print(timestamp, line)

                parts = line.split('=')
                if len(parts) > 1:
                    data = parts[1].split(',')
                    writer.writerow([timestamp] + data)

            # Rotate file every minute
            if datetime.now().strftime('%Y%m%d%H%M') != file_time.strftime('%Y%m%d%H%M'):
                file.close()
                file, writer, file_time = create_csv()

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        ser.close()
        file.close()
        print("Closed serial and file.")

if __name__ == '__main__':
    main()
