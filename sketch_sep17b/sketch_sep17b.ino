#include <Wire.h>
#include <MPU6050.h>

// Declare the MPU6050 object globally, so it's accessible in both setup() and loop()
MPU6050 mpu;
bool collecting;
void setup() {
  Serial.begin(115200);  // Start serial communication
  Wire.begin();          // Start I2C communication
  mpu.initialize();      // Initialize the MPU6050

  // Check if MPU6050 is connected properly
  if (mpu.testConnection()) {
    Serial.println("MPU6050 connection successful");
  } else {
    Serial.println("MPU6050 connection failed");
  }
}
int itr = 0;
int16_t sax, say, saz;
int16_t sgx, sgy, sgz;
void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Read input until newline
    input.trim(); // Remove any leading/trailing whitespace

    if (input.equalsIgnoreCase("c")) {
      collecting = false;
      Serial.println("Data collection stopped.");
    } else if (input.equalsIgnoreCase("z")) {
      collecting = true;
      Serial.println("Data collection started.");
    }
  }

  if (collecting) {
    int16_t ax, ay, az;
    int16_t gx, gy, gz;
    

    // Get accelerometer and gyroscope data
    mpu.getAcceleration(&ax, &ay, &az);
    mpu.getRotation(&gx, &gy, &gz);
    // if (itr == 0) {
    //   sax = ax;
    //   say = ay;
    //   saz = az;
    //   sgx = gx;
    //   sgy = gy; 
    //   sgz = gz;
    //   Serial.print("saX = "); Serial.print(sax);
    //   Serial.print(" | saY = "); Serial.print(say);
    //   Serial.print(" | saZ = "); Serial.print(saz);
    //   Serial.print(" | sgX = "); Serial.print(sgx);
    //   Serial.print(" | sgY = "); Serial.print(sgy);
    //   Serial.print(" | sgZ = "); Serial.println(sgz);
    //   }
    // else {
    //   ax -= sax;
    //   ay -= say;
    //   az -= saz;
    //   gx -= sgx;
    //   gy -= sgy;
    //   gz -= sgz;
    // }
    // Display the data
    Serial.print("aX = "); Serial.print(ax);
    Serial.print(" | aY = "); Serial.print(ay);
    Serial.print(" | aZ = "); Serial.print(az);
    Serial.print(" | gX = "); Serial.print(gx);
    Serial.print(" | gY = "); Serial.print(gy);
    Serial.print(" | gZ = "); Serial.println(gz);
    itr++;
  }

  // delay(500);  // Delay for readability
  delay(500);  // Delay for readability
}