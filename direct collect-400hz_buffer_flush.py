# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 16:26:53 2025

@author: beckylin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:44:22 2025
@author: beckylin
"""

import serial
from datetime import datetime
import csv
import os
from tkinter import simpledialog
import tkinter as tk
import time

# Initialize the serial connection
ser = serial.Serial('COM4', baudrate=115200)  # Replace 'COM4' with your actual port

# Function to create a new CSV file path and writer
def create_new_file():
    root = tk.Tk()
    root.withdraw()
    mainpath = datetime.now()
    filename = simpledialog.askstring("Input", "Enter filename to save recording (without extension):")
    if not filename:
        print("No filename entered, closing serial.")
        if ser.is_open:
            ser.close()
        exit()
    tmppath = './vibration_data/' + mainpath.strftime('%Y%m%d') + '/' + filename + ".csv"
    
    # Create directory if it doesn't exist
    if not os.path.exists('./vibration_data/' + mainpath.strftime('%Y%m%d')):
        os.makedirs('./vibration_data/' + mainpath.strftime('%Y%m%d'))
    
    file = open(tmppath, mode='a', newline='')
    writer = csv.writer(file)
    writer.writerow(['DATETIME', 'X', 'Y', 'Z'])  # Write the header row
    
    return file, writer, mainpath

# Create the initial CSV file and writer
file, writer, mainpath = create_new_file()

try:
    # Open the serial port
    if not ser.is_open:
        ser.open()

    #Flush buffer before starting measurement avoid accumulated the data to stored
    ser.reset_input_buffer()
    print("Buffer flushed.")
    print("Reading data from the serial port. Press Ctrl+C to stop.")

    pre_time = time.time()
    count = 0

    while True:
        # Read a line from the serial port
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        
        
        if line:
            # Get the current timestamp
            current_time = datetime.today().strftime('%H%M%S%f')[:9]
            
            # Split data
            value = line.split("=")

            # Write data if valid
            if len(value) == 2:
                data= value[1].split(",")
                # print(data)
                writer.writerow([current_time] + data)
            
            # Sampling rate compute
            count += 1
            now = time.time()
            if now - pre_time >= 1:
                print(f"Samples/sec: {count}")
                count = 0
                pre_time = now

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("\nStopped reading data.")

finally:
    ser.close()
    file.close()
    print("Serial port and file closed.")