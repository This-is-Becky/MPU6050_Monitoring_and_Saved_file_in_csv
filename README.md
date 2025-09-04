# MPU6050_Monitoring_and_Saved_file_in_csv
Reads accelerometer data from an MPU6050 sensor using the Adafruit library and outputs the values via the serial port in CSV format.

## Arduino setup
- Using I2C communication `(Wire.begin())` 

- Sets I2C clock speed to 400kHz for faster data transfer.```Wire.setClock(400000)```

- With 250000 baud rate ```Serial.begin(250000)```

- Read Accelerometer data ```(a.acceleration.x, y, z)```
## Arduino Serial Monitor result 
```
14:14:15.657 ->  X,Y,Z= -1.84,2.93,-9.22
14:14:15.657 ->  X,Y,Z= -2.30,2.00,-9.91
14:14:15.657 ->  X,Y,Z= -2.98,1.32,-10.18
```

## Arduino Serial Plotter result 
<img width="205" height="131" alt="image" src="https://github.com/user-attachments/assets/b2a859b1-54ce-4120-91a0-f198989cb6c0" />

## Data Logger-Python script

- Serial Communication(ports/ baud rate)
```PORT = 'COM16'```  `BAUDRATE = 250000`
- CSV Logging to saves accelerometer data (X, Y, Z) with timestamps into a CSV file.
  `def main():`
- Auto File Rotation: Creates a new CSV file every minute, organized by date and time.
```
if datetime.now().strftime('%Y%m%d%H%M') != file_time.strftime('%Y%m%d%H%M'):
                file.close()
                file, writer, file_time = create_csv()
```
- Directory Management to automatically creates folders based on the current date under ./vibration_data/.
`def create_csv():` which creates a new folder every day, and a new file every minute.

-  **`flush()`** function:
The flush() method is used to force the writing of buffered data to disk. When you write to a file, Python doesn't immediately save that data to the file — it stores it in a temporary memory area called a buffer. `flush()` clears that buffer and writes everything to the file right away.
   - To ensure data is saved immediately, especially in real-time applications like sensor logging.
   - To prevent data loss if the program crashes or is interrupted.
   - To see updates in the file instantly, useful for monitoring or debugging.

## Write-in Data-CSV result

<img width="205" height="131" alt="image" src="https://github.com/user-attachments/assets/994eee22-ddae-4233-b02a-636fcb518e42" />

## Add-in Delete file function
The **"Write_data_and_add_Delete_function.py"** is adding a delete function to prevent excessive storage usage, keeping the storage organized and efficient without manual intervention.

`def delete_folder():`

- This will scans the directory for subfolders named by date (e.g., 20230903).
- Keeps only the most recent 30 folders.
- If there are more than 30 folders, it:
   - Sorts them by date (oldest first).
   - Deletes the oldest folder to maintain the limit.
     

