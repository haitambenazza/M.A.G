#include <Arduino.h>
#include <Servo.h>

Servo base;

void setup() {
    base.attach(9, 500, 2500);
    Serial.begin(115200);
}

void loop() {
    Serial.println("0 degree");
    base.write(0);
    delay(3000);
    Serial.println("90 degree");
    base.write(90);
    delay(3000);
    Serial.println("180 degree");
    base.write(180);
    delay(3000);
}