

#include <Arduino.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

void setup() {
  Wire.begin();
  Wire.setClock(400000);
  Serial.begin(250000);


  if (!mpu.begin()) {

    Serial.println("Sensor init failed");

    while (1)

      yield();

  }

  Serial.println("Found a MPU-6050 sensor");

  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);

}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  //列出加速度值
//  Serial.print(" X,Y,Z= ");
  Serial.print(a.acceleration.x);
  Serial.print(",");
  Serial.print(a.acceleration.y);
  Serial.print(",");
  Serial.print(a.acceleration.z);
  Serial.println();


}
