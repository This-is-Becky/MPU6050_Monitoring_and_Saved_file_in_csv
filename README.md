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


## CSV result

<img width="205" height="131" alt="image" src="https://github.com/user-attachments/assets/994eee22-ddae-4233-b02a-636fcb518e42" />
