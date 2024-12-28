// Basic demo for accelerometer readings from Adafruit MPU6050

// ESP32 Guide: https://RandomNerdTutorials.com/esp32-mpu-6050-accelerometer-gyroscope-arduino/
// ESP8266 Guide: https://RandomNerdTutorials.com/esp8266-nodemcu-mpu-6050-accelerometer-gyroscope-arduino/
// Arduino Guide: https://RandomNerdTutorials.com/arduino-mpu-6050-accelerometer-gyroscope/

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
bool collecting;
bool first_round;

void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }

  Serial.println("");
  Serial.println("Setup complete!");
  delay(100);
}

void loop() {
  /* Get new sensor events with the readings */
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Read input until newline
    input.trim(); // Remove any leading/trailing whitespace

    if (input.equalsIgnoreCase("c")) {
      collecting = false;
      Serial.println("Data collection stopped.");
    } else if (input.equalsIgnoreCase("z")) {
      collecting = true;
      first_round = true;
      Serial.println("Data collection started.");
    }
  }
  if (collecting) {
    if (first_round) {
      // purely for logging purposes to make sure can line up consoles
      Serial.print("BEGINNING\n");
      first_round = false;
    }
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    // Serial.print("BEGINNING\n");
    /* Print out the values */
    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");

    Serial.print("Temperature: ");
    Serial.print(temp.temperature);
    Serial.println(" degC");

    Serial.println("");
    delay(500);
  }
}

/*

This is based on our version 1 using a different MPU6050 library.

*/

// #include <Wire.h>
// #include <MPU6050.h>

// // Declare the MPU6050 object globally, so it's accessible in both setup() and loop()
// MPU6050 mpu;
// bool collecting;
// void setup() {
//   Serial.begin(115200);  // Start serial communication
//   Wire.begin();          // Start I2C communication
//   mpu.initialize();      // Initialize the MPU6050

//   // Check if MPU6050 is connected properly
//   if (mpu.testConnection()) {
//     Serial.println("MPU6050 connection successful");
//   } else {
//     Serial.println("MPU6050 connection failed");
//   }
// }
// int itr = 0;
// int16_t sax, say, saz;
// int16_t sgx, sgy, sgz;
// void loop() {
//   if (Serial.available() > 0) {
//     String input = Serial.readStringUntil('\n'); // Read input until newline
//     input.trim(); // Remove any leading/trailing whitespace

//     if (input.equalsIgnoreCase("c")) {
//       collecting = false;
//       Serial.println("Data collection stopped.");
//     } else if (input.equalsIgnoreCase("z")) {
//       collecting = true;
//       Serial.println("Data collection started.");
//     }
//   }

//   if (collecting) {
//     int16_t ax, ay, az;
//     int16_t gx, gy, gz;
    

//     // Get accelerometer and gyroscope data
//     mpu.getAcceleration(&ax, &ay, &az);
//     mpu.getRotation(&gx, &gy, &gz);
//     // if (itr == 0) {
//     //   sax = ax;
//     //   say = ay;
//     //   saz = az;
//     //   sgx = gx;
//     //   sgy = gy; 
//     //   sgz = gz;
//     //   Serial.print("saX = "); Serial.print(sax);
//     //   Serial.print(" | saY = "); Serial.print(say);
//     //   Serial.print(" | saZ = "); Serial.print(saz);
//     //   Serial.print(" | sgX = "); Serial.print(sgx);
//     //   Serial.print(" | sgY = "); Serial.print(sgy);
//     //   Serial.print(" | sgZ = "); Serial.println(sgz);
//     //   }
//     // else {
//     //   ax -= sax;
//     //   ay -= say;
//     //   az -= saz;
//     //   gx -= sgx;
//     //   gy -= sgy;
//     //   gz -= sgz;
//     // }
//     // Display the data
//     Serial.print("aX = "); Serial.print(ax);
//     Serial.print(" | aY = "); Serial.print(ay);
//     Serial.print(" | aZ = "); Serial.print(az);
//     Serial.print(" | gX = "); Serial.print(gx);
//     Serial.print(" | gY = "); Serial.print(gy);
//     Serial.print(" | gZ = "); Serial.println(gz);
//     itr++;
//   }

//   // delay(500);  // Delay for readability
//   delay(500);  // Delay for readability
// }