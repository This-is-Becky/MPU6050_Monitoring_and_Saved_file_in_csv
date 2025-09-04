# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 14:28:16 2023

@author: beckylin
"""

import serial
from datetime import datetime
import csv
import os
import shutil

# Settings
PORT = 'COM16'
BAUDRATE = 115200
DATA_DIR = './vibration_data'
thersold_folder = 30

def create_csv():
    now = datetime.now()
    folder = os.path.join(DATA_DIR, now.strftime('%Y%m%d'))
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, now.strftime('%Y%m%d%H%M') + '.csv')
    file = open(filename, 'a', newline='')
    writer = csv.writer(file)
    writer.writerow(['DATETIME', 'X', 'Y', 'Z'])
    return file, writer, now

def delete_folder():
    """Delete the oldest folder if there are more than 30 folders."""
    path = DATA_DIR
    items = os.listdir(path)
    directories = [os.path.join(path, item) for item in items if os.path.isdir(os.path.join(path, item))]
    
    if len(directories) > thersold_folder:
        try:
            # Sort by folder name assuming format YYYYMMDD
            directories.sort(key=lambda x: datetime.strptime(os.path.basename(x), '%Y%m%d'))
            shutil.rmtree(directories[0])
            print(f"Deleted old folder: {directories[0]}")
        except Exception as e:
            print(f"Error deleting folder: {e}")

def main():
    ser = serial.Serial(PORT, BAUDRATE)
    file, writer, file_time = create_csv()
    delete_folder()  # Clean up if too many folders

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
                delete_folder()

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        ser.close()
        file.close()
        print("Closed serial and file.")

if __name__ == '__main__':
    main()
