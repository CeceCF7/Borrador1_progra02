#include <ESP32Servo.h>. 

const int trigPin = 33;
const int echoPin = 25; 

long duration;
int distance;

Servo myServo1;

Servo myServo2;  

void setup() {
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);
  Serial.begin(115200);
  myServo1.attach(27);
  myServo2.attach(26);  
}

void loop() {

  myServo2.write(0);

  for(int i=0;i<=130;i++){  
  myServo1.write(i);
  delay(30);
  distance = calculateDistance();
  
  Serial.print(i); 
  Serial.print(","); 
  Serial.print(distance); 
  Serial.print("."); 
  }
  // movimiento del motorcito
  
  for(int i=0;i<=15;i++){  
  myServo2.write(i);
  delay(30);
  }

  // repetición
  for(int i=130;i>0;i--){  
  myServo1.write(i);
  delay(30);
  distance = calculateDistance();
  Serial.print(i);
  Serial.print(",");
  Serial.print(distance);
  Serial.print(".");
  }

  for(int i=15;i<=30;i++){  
  myServo2.write(i);
  delay(30);
  }

  for(int i=0;i<=130;i++){  
  myServo1.write(i);
  delay(30);
  distance = calculateDistance();
  
  Serial.print(i); 
  Serial.print(","); 
  Serial.print(distance); 
  Serial.print("."); 
  }
  // movimiento del motorcito
  
  for(int i=30;i>=15;i--){
  myServo2.write(i);
  delay(30);
  }

  // repetición
  for(int i=130;i>0;i--){  
  myServo1.write(i);
  delay(30);
  distance = calculateDistance();
  Serial.print(i);
  Serial.print(",");
  Serial.print(distance);
  Serial.print(".");
  }

  for(int i=15;i>=0;i--){  
  myServo2.write(i);
  delay(30);
  }

}

int calculateDistance(){ 
  
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); 
  distance= duration*0.034/2;
  return distance;
}